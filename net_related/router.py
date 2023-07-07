from collections import deque
from typing import List, Union
from collections.abc import Iterable

import psycopg2

from DQN.agent import DQN
from data import CommunicationData, CalculateData, SensorData

# 连接到PostgresSQL数据库
conn_with_router = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)


class Router:
    def __init__(self, sign: int, storage: int = 15000, computing_power: int = 100, bandwidth: int = 500):
        self.sign: int = sign  # 路由器的序号
        self.storage: float = storage
        self.computing_power: float = computing_power
        self.bandwidth: int = bandwidth
        self.distribution = {
            1: {  # bandwidth
                1: -1,
                2: -1,
                3: -1
            },
            2: {  # computing_power
                1: -1,
                2: -1,
                3: -1
            },
            3: {  # storage
                1: -1,
                2: -1,
                3: -1
            }
        }
        self.state = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.agent = DQN((3, 3), 10)
        """与通信相关的参数"""
        self.cache_queue_communication = deque()
        self.communication_cache_slice_1: int = 0
        self.communication_cache_slice_2: int = 0
        self.communication_cache_slice_3: int = 0
        self.communication_load_slice = {
            1: self.communication_cache_slice_1,
            2: self.communication_cache_slice_2,
            3: self.communication_cache_slice_3
        }
        self.communication_successful_data = 0
        self.communication_loss_data = 0
        """与计算相关的参数"""
        self.calculate_queue = deque()
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

    def __repr__(self):
        return f'Router:{self.sign}'

    def __str__(self):
        return f'Router:{self.sign}'

    def pop_data_communication(self) -> Union[List[CommunicationData], None]:
        data_list: List[CommunicationData] = []
        # 创建一个游标对象
        cursor = conn_with_router.cursor()
        waiting_time = 0
        while self.cache_queue_communication:
            data: CommunicationData = self.cache_queue_communication.pop()
            """释放对应切片在通信资源上的负载"""
            self.communication_load_slice[data.slice_sign] -= data.bandwidth_required
            """添加时延信息，dataset.delay指的是数据包在上一段链路上的时延"""
            waiting_time += data.bandwidth_required / (self.bandwidth * self.distribution[1][data.slice_sign])
            data.delay_every_step.append(waiting_time + data.delay)
            """对已到达终点的数据包进行特殊处理"""
            if data.path[-1] == self.sign:
                """代表数据包一路上经过的路由器序号"""
                index = 0
                """将时延信息存入数据包"""
                # 执行插入数据的SQL语句
                sql = 'INSERT INTO "CommunicationDataDB"(id, start_router_sign, end_router_sign, delay, ' \
                      'slice_sign, is_loss)' \
                      'VALUES (%s, %s, %s, %s, %s, %s)'
                for item_delay in data.delay_every_step:
                    values = (data.sign, data.path[index], data.path[index + 1], item_delay, data.slice_sign, False)
                    cursor.execute(sql, values)
                    index += 1
                """数据包成功传输，成功运输的数据包数量加1"""
                self.communication_successful_data += 1
                del data
            else:
                data_list.append(data)
            # 提交事务
            conn_with_router.commit()
        # 关闭游标
        cursor.close()
        """有数据传数据，没数据传None"""
        if data_list:
            return data_list
        else:
            return None

    def push_data_communication(self, data_list: List[CommunicationData]):
        # 创建一个游标对象
        cursor = conn_with_router.cursor()
        for data in data_list:
            """更新数据包状态，为下一次转发做准备"""
            data.current_router = self.sign
            """将数据包添加到通信队列"""
            self.cache_queue_communication.append(data)
            """添加指定切片在通信资源上的负载"""
            if self.communication_load_slice[data.slice_sign] + data.bandwidth_required <= \
                    (self.distribution[1][data.slice_sign] * self.bandwidth):
                self.communication_load_slice[data.slice_sign] += data.bandwidth_required
            else:
                """代表数据包一路上经过的路由器序号"""
                index = 0
                """将时延信息存入数据包"""
                # 执行插入数据的SQL语句
                sql = 'INSERT INTO "CommunicationDataDB"' \
                      '(id, start_router_sign, end_router_sign, delay, slice_sign, is_loss)' \
                      'VALUES (%s, %s, %s, %s, %s, %s)'
                for item_delay in data.delay_every_step:
                    values = (data.sign, data.path[index], data.path[index + 1], item_delay, data.slice_sign, True)
                    cursor.execute(sql, values)
                    index += 1
                """负载容量不够，数据包丢失，统计数据"""
                self.communication_loss_data += 1
                del data

    def deal_calculate_task(self):
        # 创建一个游标对象
        cursor = conn_with_router.cursor()
        waiting_time = 0
        while self.calculate_queue:
            data: CalculateData = self.calculate_queue.pop()
            waiting_time += data.calculate_required / (self.distribution[2][data.slice_sign] * self.computing_power)
            sql = 'INSERT INTO "CalculateDataDB" (id, router_id, delay, slice_sign)  ' \
                  'VALUES (%s, %s, %s, %s)'
            values = (data.sign, self.sign, waiting_time, data.slice_sign)
            cursor.execute(sql, values)
            del data
        # 提交事务
        conn_with_router.commit()
        # 关闭游标
        cursor.close()

    def push_calculate_task(self, tasks: Union[CalculateData, List[CalculateData]]):
        if isinstance(tasks, Iterable):
            self.calculate_queue.extend(tasks)
        else:
            self.calculate_queue.append(tasks)

    def push_sensor_data(self, dataset: Union[SensorData, List[SensorData]]):
        # 创建一个游标对象
        cursor = conn_with_router.cursor()
        if isinstance(dataset, Iterable):
            for task in dataset:
                """存储资源不够则丢包，够则存储"""
                if task.storage_required + self.sensor_load_slice[task.slice_sign] <= \
                        (self.distribution[3][task.slice_sign] * self.storage):
                    self.sensor_queue.append(task)
                else:
                    self.sensor_loss_number += 1
                    sql = 'INSERT INTO "SensorDataDB" (id, router_id, slice_id, is_loss)  ' \
                          'VALUES (%s, %s, %s, %s)'
                    values = (task.unique_sign, self.sign, task.slice_sign, True)
                    cursor.execute(sql, values)
                    del task
        else:
            if dataset.storage_required + self.sensor_load_slice[dataset.slice_sign] <= \
                    (self.distribution[3][dataset.slice_sign] * self.storage):
                self.calculate_queue.append(dataset)
            else:
                self.sensor_loss_number += 1
                sql = 'INSERT INTO "SensorDataDB" (id, router_id, slice_id, is_loss)  ' \
                      'VALUES (%s, %s, %s, %s)'
                values = (dataset.sign, self.sign, dataset.slice_sign, True)
                cursor.execute(sql, values)
                del dataset
        # 提交事务
        conn_with_router.commit()
        # 关闭游标
        cursor.close()

    def deal_sensor_data(self):
        while self.sensor_queue:
            # 创建一个游标对象
            cursor = conn_with_router.cursor()
            """临时承载数据包"""
            temporary_list: List[SensorData] = []
            data: SensorData = self.sensor_queue.pop()
            data.count -= 1
            """三次标记不够继续存储"""
            if data.count > 0:
                temporary_list.append(data)
            else:
                """否则销毁该数据，并且记做该数据成功完成任务，存入数据库"""
                self.sensor_success_number += 1
                sql = 'INSERT INTO "SensorDataDB" (id, router_id, slice_id, is_loss)  ' \
                      'VALUES (%s, %s, %s, %s)'
                values = (data.sign, self.sign, data.slice_sign, False)
                cursor.execute(sql, values)
                del data
            self.sensor_queue.extend(temporary_list)
            # 提交事务
            conn_with_router.commit()
            # 关闭游标
            cursor.close()
