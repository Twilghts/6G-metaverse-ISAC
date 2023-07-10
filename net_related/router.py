import copy
from collections import deque
from collections.abc import Iterable
from typing import List, Union, Dict

import numpy as np
import psycopg2

import calculatetask
import communicationtask
import methods
import sensortask
from DQN.agent import DQN
from data import CommunicationData, CalculateData, SensorData
from task import Task

# 连接到PostgresSQL数据库
conn_with_router = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
# 创建一个游标对象
cursor = conn_with_router.cursor()
# 执行插入数据的SQL语句
sql_communication = 'INSERT INTO "CommunicationDataDB"(id, router_sign, delay, slice_sign, is_loss )' \
                    'VALUES (%s, %s, %s, %s, %s)'

sql_calculate = 'INSERT INTO "CalculateDataDB" (id, router_id, delay, slice_sign)  ' \
                'VALUES (%s, %s, %s, %s)'

sql_sensor = 'INSERT INTO "SensorDataDB" (id, router_id, slice_id, is_loss)  ' \
             'VALUES (%s, %s, %s, %s)'


class Router:
    def __init__(self, sign: int, storage: int = 15000, computing_power: int = 100, bandwidth: int = 500):
        self.sign: int = sign  # 路由器的序号
        self.storage: float = storage
        self.computing_power: float = computing_power
        self.bandwidth: int = bandwidth
        self.distribution: Dict[int, Dict[int, float]] = {
            1: {  # bandwidth
                1: -1,  # 切片一
                2: -1,  # 切片二
                3: -1  # 切片三
            },
            2: {  # computing_power
                1: -1,  # 切片一
                2: -1,  # 切片二
                3: -1  # 切片三
            },
            3: {  # storage
                1: -1,  # 切片一
                2: -1,  # 切片二
                3: -1  # 切片三
            }
        }
        self.state: List[List[Union[float, None]]] = [[-2, -1, -1], [-1, -1, -1], [None, None, None]]
        self.agent = DQN((3, 3))
        self.action_index = None  # 记载智能体的action的索引
        """与通信相关的参数"""
        self.cache_queue_communication = deque()
        self.communication_cache_slice_1: int = 0
        self.communication_cache_slice_2: int = 0
        self.communication_cache_slice_3: int = 0
        self.communication_load: Dict[int, int] = {
            1: self.communication_cache_slice_1,
            2: self.communication_cache_slice_2,
            3: self.communication_cache_slice_3
        }
        self.communication_reward_log: Dict[int, List[float]] = {
            1: [],
            2: [],
            3: []
        }
        self.communication_successful_data = 0
        self.communication_loss_data = 0
        """与计算相关的参数"""
        self.calculate_queue = deque()
        self.calculate_reward_log: Dict[int, List[float]] = {
            1: [],
            2: [],
            3: []
        }
        """与存储相关的参数"""
        self.sensor_queue = deque()
        self.sensor_success_number = 0
        self.sensor_loss_number = 0
        self.sensor_cache_slice_1: int = 0
        self.sensor_cache_slice_2: int = 0
        self.sensor_cache_slice_3: int = 0
        self.sensor_load_slice = {
            1: self.sensor_cache_slice_1,
            2: self.sensor_cache_slice_2,
            3: self.sensor_cache_slice_3
        }
        self.sensor_reward_log: Dict[int, Union[None, bool]] = {
            1: None,
            2: None,
            3: None
        }

    def __repr__(self):
        return f'Router:{self.sign},带宽资源为:{self.bandwidth},计算资源为:{self.computing_power},存储资源为:{self.storage}'

    def __str__(self):
        return f'Router:{self.sign},带宽资源为:{self.bandwidth},计算资源为:{self.computing_power},存储资源为:{self.storage}'

    def markov(self):
        """更新状态，选择动作，计算奖励，向回放缓存中添加数据，完成一次马尔可夫过程，处理部分数据"""
        """以下为计算奖励值的过程"""
        sensor_slice_1 = self.sensor_reward_log[1]
        self.sensor_reward_log[1] = None
        sensor_slice_2 = self.sensor_reward_log[2]
        self.sensor_reward_log[2] = None
        sensor_slice_3 = self.sensor_reward_log[3]
        self.sensor_reward_log[3] = None
        if self.communication_reward_log[1]:
            communication_slice_1 = sum(self.communication_reward_log[1]) / len(self.communication_reward_log[1])
            self.communication_reward_log[1].clear()
        else:
            communication_slice_1 = -1
        if self.communication_reward_log[2]:
            communication_slice_2 = sum(self.communication_reward_log[2]) / len(self.communication_reward_log[2])
            self.communication_reward_log[2].clear()
        else:
            communication_slice_2 = -1
        if self.communication_reward_log[3]:
            communication_slice_3 = sum(self.communication_reward_log[3]) / len(self.communication_reward_log[3])
            self.communication_reward_log[3].clear()
        else:
            communication_slice_3 = -1
        if self.calculate_reward_log[1]:
            calculate_slice_1 = sum(self.calculate_reward_log[1]) / len(self.calculate_reward_log[1])
            self.calculate_reward_log[1].clear()
        else:
            calculate_slice_1 = -1
        if self.calculate_reward_log[2]:
            calculate_slice_2 = sum(self.calculate_reward_log[2]) / len(self.calculate_reward_log[2])
            self.calculate_reward_log[2].clear()
        else:
            calculate_slice_2 = -1
        if self.calculate_reward_log[3]:
            calculate_slice_3 = sum(self.calculate_reward_log[3]) / len(self.calculate_reward_log[3])
            self.calculate_reward_log[3].clear()
        else:
            calculate_slice_3 = -1
        reword = methods.reword(((communication_slice_1, communication_slice_2, communication_slice_3),
                                 (calculate_slice_1, calculate_slice_2, calculate_slice_3),
                                 (sensor_slice_1, sensor_slice_2, sensor_slice_3)))
        """以下为计算状态的过程,计算奖励值的参数即为状态，即根据状态得出奖励值"""
        state = copy.deepcopy(self.state)
        state[0][0] = communication_slice_1
        state[0][1] = communication_slice_2
        state[0][1] = communication_slice_3
        state[1][0] = calculate_slice_1
        state[1][1] = calculate_slice_2
        state[1][2] = calculate_slice_3
        if sensor_slice_1 is None or sensor_slice_1 is False:
            state[2][0] = 1
        else:
            state[2][0] = 0
        if sensor_slice_2 is None or sensor_slice_2 is False:
            state[2][1] = 1
        else:
            state[2][1] = 0
        if sensor_slice_3 is None or sensor_slice_3 is False:
            state[2][2] = 1
        else:
            state[2][2] = 0
        """如果智能体第一次运行则不向回放缓存中存储信息，只更新当前状态，动作和应用这次动作"""
        if self.state[0][0] == -2:
            self.state = copy.deepcopy(state)
            action, self.action_index = self.agent.act(np.array(self.state).reshape(1, 9))
            self.apply_action(action=action)
            return 42
        else:
            self.agent.remember(np.array(self.state).reshape(1, 9), self.action_index,
                                reword, np.array(state).reshape(1, 9))
            self.state = copy.deepcopy(state)
            action, self.action_index = self.agent.act(np.array(self.state).reshape(1, 9))
            self.apply_action(action=action)

    def apply_action(self, action: List[List[float]]):
        """处理上一个状态遗留下来的数据，并且利用动作更新分配标准"""
        self.pop_data_communication()
        self.deal_calculate_task()
        self.deal_sensor_data()
        for row in range(1, 4):
            for col in range(1, 4):
                self.distribution[row][col] = action[row - 1][col - 1]

    def put_task(self, task: Task):
        if isinstance(task, communicationtask.CommunicationTask):
            self.push_data_communication(task.dataset)
        elif isinstance(task, calculatetask.CalculateTask):
            self.push_calculate_task(task.dataset)
        elif isinstance(task, sensortask.SensorTask):
            self.push_sensor_data(task.dataset)

    def pop_data_communication(self) -> Union[List[CommunicationData], None]:
        data_list: List[CommunicationData] = []
        waiting_time = 0
        values = []
        while self.cache_queue_communication:
            data: CommunicationData = self.cache_queue_communication.pop()
            """释放对应切片在通信资源上的负载"""
            self.communication_load[data.slice_sign] -= data.bandwidth_required
            """添加时延信息，dataset.delay指的是数据包在上一段链路上的时延"""
            waiting_time += data.bandwidth_required / (self.bandwidth * self.distribution[1][data.slice_sign])
            data.delay_every_step.append(waiting_time + data.delay)
            """为计算奖励值做准备"""
            self.communication_reward_log[data.slice_sign].append(waiting_time + data.delay)
            """对已到达终点的数据包进行特殊处理"""
            if data.path[-1] == self.sign:
                """代表数据包一路上经过的路由器序号"""
                index = 0
                """将时延信息存入数据包"""
                for item_delay in data.delay_every_step:
                    value = (data.sign, data.path[index], item_delay, data.slice_sign, False)
                    values.append(value)
                    index += 1
                """数据包成功传输，成功运输的数据包数量加1"""
                self.communication_successful_data += 1
                del data
            else:
                data_list.append(data)
        """有数据传数据，没数据传None"""
        if data_list:
            cursor.executemany(sql_communication, values)
            conn_with_router.commit()
            return data_list
        else:
            return None

    def push_data_communication(self, data_list: Union[List[CommunicationData], CommunicationData]):
        """如果是单个的数据包就单独处理"""
        values = []
        if not isinstance(data_list, Iterable):
            """更新数据包状态，为下一次转发做准备"""
            data_list.current_router = self.sign
            """添加指定切片在通信资源上的负载"""
            if self.communication_load[data_list.slice_sign] + data_list.bandwidth_required <= \
                    (self.distribution[1][data_list.slice_sign] * self.bandwidth):
                self.communication_load[data_list.slice_sign] += data_list.bandwidth_required
                """将数据包添加到通信队列"""
                self.cache_queue_communication.append(data_list)
            else:
                """代表数据包一路上经过的路由器序号"""
                index = 0
                """将时延信息存入数据包"""  # 执行插入数据的SQL语句
                for item_delay in data_list.delay_every_step:
                    value = (data_list.sign, data_list.path[index], item_delay, data_list.slice_sign, True)
                    values.append(value)
                    index += 1
                cursor.executemany(sql_communication, values)
                """负载容量不够，数据包丢失，统计数据"""
                self.communication_loss_data += 1
                del data_list
        else:
            for data in data_list:
                """更新数据包状态，为下一次转发做准备"""
                data.current_router = self.sign
                """添加指定切片在通信资源上的负载"""
                if self.communication_load[data.slice_sign] + data.bandwidth_required <= \
                        (self.distribution[1][data.slice_sign] * self.bandwidth):
                    self.communication_load[data.slice_sign] += data.bandwidth_required
                    """将数据包添加到通信队列"""
                    self.cache_queue_communication.append(data)
                else:
                    """代表数据包一路上经过的路由器序号"""
                    index = 0
                    """将时延信息存入数据包"""
                    for item_delay in data.delay_every_step:
                        value = (data.sign, data.path[index], item_delay, data.slice_sign, True)
                        values.append(value)
                        index += 1
                    """负载容量不够，数据包丢失，统计数据"""
                    self.communication_loss_data += 1
                    del data
            cursor.executemany(sql_communication, values)
        conn_with_router.commit()

    def deal_calculate_task(self):
        waiting_time = 0
        values = []
        while self.calculate_queue:
            data: CalculateData = self.calculate_queue.pop()
            waiting_time += data.calculate_required / (self.distribution[2][data.slice_sign] * self.computing_power)
            """为计算奖励值做准备"""
            self.calculate_reward_log[data.slice_sign].append(waiting_time)
            value = (data.sign, self.sign, waiting_time, data.slice_sign)
            values.append(value)
            del data
        if values:
            cursor.executemany(sql_calculate, values)
            conn_with_router.commit()

    def push_calculate_task(self, tasks: Union[CalculateData, List[CalculateData]]):
        if isinstance(tasks, Iterable):
            self.calculate_queue.extend(tasks)
        else:
            self.calculate_queue.append(tasks)

    def push_sensor_data(self, dataset: Union[SensorData, List[SensorData]]):
        if isinstance(dataset, Iterable):
            values = []
            for task in dataset:
                """存储资源不够则丢包，够则存储"""
                if task.storage_required + self.sensor_load_slice[task.slice_sign] <= \
                        (self.distribution[3][task.slice_sign] * self.storage):
                    self.sensor_queue.append(task)
                else:
                    self.sensor_loss_number += 1
                    """为计算奖励值做准备"""
                    self.sensor_reward_log[task.slice_sign] = True
                    value = (task.sign, self.sign, task.slice_sign, True)
                    values.append(value)
                    del task
            cursor.executemany(sql_sensor, values)
        else:
            if dataset.storage_required + self.sensor_load_slice[dataset.slice_sign] <= \
                    (self.distribution[3][dataset.slice_sign] * self.storage):
                self.calculate_queue.append(dataset)
            else:
                self.sensor_loss_number += 1
                """为计算奖励值做准备"""
                self.sensor_reward_log[dataset.slice_sign] = True
                cursor.execute(sql_sensor, (dataset.sign, self.sign, dataset.slice_sign, True))
                del dataset
        conn_with_router.commit()

    def deal_sensor_data(self):
        values = []
        temporary_list: List[SensorData] = []
        while self.sensor_queue:
            """临时承载数据包"""
            data: SensorData = self.sensor_queue.pop()
            data.count -= 1
            """三次标记不够继续存储"""
            if data.count > 0:
                temporary_list.append(data)
            else:
                """否则销毁该数据，并且记做该数据成功完成任务，存入数据库"""
                self.sensor_success_number += 1
                value = (data.sign, self.sign, data.slice_sign, False)
                values.append(value)
                del data
        self.sensor_queue.extend(temporary_list)
        if values:
            cursor.executemany(sql_sensor, values)
            conn_with_router.commit()
