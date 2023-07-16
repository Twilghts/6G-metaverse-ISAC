import random
import time
from typing import Set, Dict, List, Union, Tuple

import psutil
import psycopg2

import communicationtask
from net_related.net import Net
from service.servicefactory import TaskFactory, TypeOfTask
from service.task import Task


def registration_db(sql, values, conn, cursor):
    cursor.executemany(sql, values)
    conn.commit()


def build_task_set(_number: int, _paths: Dict[int, List[List[int]]], _task_id: int, _data_id: int) \
        -> Tuple[Set[Task], int, int]:
    _task_set = set()
    objects = {
        1: TypeOfTask.communication_task,
        2: TypeOfTask.calculate_task,
        3: TypeOfTask.sensor_task
    }
    path = None
    for _i in range(_number):
        _random_number = random.randint(1, 3)
        _slice_number = random_slice(_random_number)
        if _random_number == 1:
            path: Union[List[int], None] = random.choice(_paths[_slice_number])
        _task = TaskFactory.create_task(objects[_random_number],
                                        slice_sign=_slice_number, path=path, task_id=_task_id, data_id=_data_id)
        _task_set.add(_task)
        _task_id, _data_id = _task.task_id, _task.data_id
    return _task_set, _task_id, _data_id


def random_slice(_number: int):
    random_numbers = [1, 2, 3]
    random_numbers.remove(_number)
    if random.random() < 0.7:
        return _number
    else:
        return random.choice(random_numbers)


if __name__ == '__main__':
    _conn_in_train = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="rkw2536153"
    )
    _cursor_pool = []
    for number in range(50):
        _cursor_pool.append(_conn_in_train.cursor())
    _update_keyvalue_task = "UPDATE keyvalues_zhang SET value = %s WHERE key = 'taskid'"
    _update_keyvalue_data = "UPDATE keyvalues_zhang SET value = %s WHERE key = 'dataid'"

    _sql_communication = 'INSERT INTO "communicationdatadb_zhang"(id, timestamp,  router_sign, delay, slice_sign, is_loss )' \
                         'VALUES (%s, %s, %s, %s, %s, %s)'

    _sql_calculate = 'INSERT INTO "calculatedatadb_zhang" (id, time,  router_id, delay, slice_sign)  ' \
                     'VALUES (%s, %s, %s, %s, %s)'

    _sql_sensor = 'INSERT INTO "sensordatadb_zhang" (id, time,  router_id, slice_id, is_loss)  ' \
                  'VALUES (%s, %s, %s, %s, %s)'

    _cursor_pool[0].execute("SELECT value FROM keyvalues_zhang where key = 'taskid'")
    task_id = _cursor_pool[0].fetchone()[0]
    _cursor_pool[0].execute("SELECT value FROM keyvalues_zhang where key = 'dataid'")
    data_id = _cursor_pool[0].fetchone()[0]
    start_time = time.perf_counter()
    net = Net()
    net.initialize()
    paths = net.chose_paths()
    task_set, task_id, data_id = build_task_set(200, paths, _task_id=task_id, _data_id=data_id)
    """准备数据"""
    for i in range(170):
        for j in range(50):
            task = task_set.pop()
            if isinstance(task, communicationtask.CommunicationTask):
                net.routers[task.path[0]].put_task(task)
            else:
                random.choice(list(net.routers.values())).put_task(task)
            if j == 25:
                net.deal_data()
        for router in net.routers.values():
            router.markov()
        """改变链路的带宽资源分配情况"""
        net.act_in_links()
        """选择通信链路的任务路径"""
        paths = net.chose_paths()
        tem_set, task_id, data_id = build_task_set(50, paths, _task_id=task_id, _data_id=data_id)
        task_set |= tem_set
        del tem_set

    print(f"准备工作消耗时间:{time.perf_counter() - start_time}")
    for total_epoch in range(1000):
        print(f"第{total_epoch}轮")
        for router in net.routers.values():
            router.agent.build_dataset()
        for router in net.routers.values():
            router.agent.replay()
        for i in range(75):
            for j in range(50):
                task = task_set.pop()
                if isinstance(task, communicationtask.CommunicationTask):
                    net.routers[task.path[0]].put_task(task)
                else:
                    random.choice(list(net.routers.values())).put_task(task)
                if j == 25:
                    net.deal_data()
            for router in net.routers.values():
                router.markov()
            """改变链路的带宽资源分配情况"""
            net.act_in_links()
            """选择通信链路的任务路径"""
            paths = net.chose_paths()
            tem_set, task_id, data_id = build_task_set(75, paths, _task_id=task_id, _data_id=data_id)
            task_set |= tem_set
            del tem_set
        print(time.perf_counter() - start_time)
        memory_usage = psutil.virtual_memory()
        print(f"Memory Usage: {memory_usage.percent}%")
        if memory_usage.percent >= 80:
            for router in net.routers.values():
                registration_db(_sql_communication, router.communication_values, _conn_in_train,
                                random.choice(_cursor_pool))
                router.communication_values.clear()
                registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
                router.calculate_values.clear()
                registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
                router.sensor_values.clear()
    """全部结束后的统一信息存储"""
    for router in net.routers.values():
        registration_db(_sql_communication, router.communication_values, _conn_in_train, random.choice(_cursor_pool))
        router.communication_values.clear()
        registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
        router.calculate_values.clear()
        registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
        router.sensor_values.clear()
        filename = "model_7_" + str(router.sign)
        router.agent.target_model.save(f"../resource/{filename}")
    _cursor_pool[0].execute(_update_keyvalue_task, (task_id,))
    _cursor_pool[0].execute(_update_keyvalue_data, (data_id,))
    _conn_in_train.commit()
    print(time.perf_counter() - start_time)