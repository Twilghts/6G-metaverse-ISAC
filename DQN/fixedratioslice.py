import random
import time

import psutil
import psycopg2

import communicationtask
from net import Net
from train import build_task_set, registration_db

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
    _update_keyvalue_task = "UPDATE keyvalues_comparison SET value = %s WHERE key = 'taskid'"
    _update_keyvalue_data = "UPDATE keyvalues_comparison SET value = %s WHERE key = 'dataid'"

    _sql_communication = 'INSERT INTO "communicationdatadb_comparison"(id, router_sign, delay, slice_sign, is_loss )' \
                         'VALUES (%s, %s, %s, %s, %s)'

    _sql_calculate = 'INSERT INTO "calculatedatadb_comparison" (id, router_id, delay, slice_sign)  ' \
                     'VALUES (%s, %s, %s, %s)'

    _sql_sensor = 'INSERT INTO "sensordatadb_comparison" (id, router_id, slice_id, is_loss)  ' \
                  'VALUES (%s, %s, %s, %s)'

    _cursor_pool[0].execute("SELECT value FROM keyvalues_comparison where key = 'taskid'")
    task_id = _cursor_pool[0].fetchone()[0]
    _cursor_pool[0].execute("SELECT value FROM keyvalues_comparison where key = 'dataid'")
    data_id = _cursor_pool[0].fetchone()[0]
    start_time = time.perf_counter()
    net = Net()
    net.initialize()
    paths = net.chose_paths()
    task_set, task_id, data_id = build_task_set(200, paths, _task_id=task_id, _data_id=data_id)
    for i in range(4000000):
        task = task_set.pop()
        if isinstance(task, communicationtask.CommunicationTask):
            net.routers[task.path[0]].put_task(task)
        else:
            random.choice(list(net.routers.values())).put_task(task)
        if i % 25 == 0 and i != 0:
            net.deal_data()
        if i % 50 == 0 and i != 0:
            for router in net.routers.values():
                router.markov(is_dqn=False)
            """选择通信链路的任务路径"""
            paths = net.chose_paths()
            tem_set, task_id, data_id = build_task_set(50, paths, _task_id=task_id, _data_id=data_id)
            task_set |= tem_set
            del tem_set
        memory_usage = psutil.virtual_memory()
        if memory_usage.percent >= 80:
            for router in net.routers.values():
                registration_db(_sql_communication, router.communication_values, _conn_in_train,
                                random.choice(_cursor_pool))
                router.communication_values.clear()
                registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
                router.calculate_values.clear()
                registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
                router.sensor_values.clear()
    for router in net.routers.values():
        registration_db(_sql_communication, router.communication_values, _conn_in_train, random.choice(_cursor_pool))
        router.communication_values.clear()
        registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
        router.calculate_values.clear()
        registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
        router.sensor_values.clear()
    _cursor_pool[0].execute(_update_keyvalue_task, (task_id,))
    _cursor_pool[0].execute(_update_keyvalue_data, (data_id,))
    _conn_in_train.commit()
