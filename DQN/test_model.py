import random
import time

import psutil
import psycopg2
import tensorflow as tf

import communicationtask
import sensortask
from net_related.net import Net
from train import build_task_set, registration_db, choose_router_index_by_calculate_weight

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
    _update_keyvalue_task = "UPDATE keyvalues SET value = %s WHERE key = 'taskid'"
    _update_keyvalue_data = "UPDATE keyvalues SET value = %s WHERE key = 'dataid'"

    _sql_communication = 'INSERT INTO "communicationdatadb"(id, timestamp,  router_sign, delay, slice_sign, is_loss )' \
                         'VALUES (%s, %s, %s, %s, %s, %s)'

    _sql_calculate = 'INSERT INTO "calculatedatadb" (id, time,  router_id, delay, slice_sign)  ' \
                     'VALUES (%s, %s, %s, %s, %s)'

    _sql_sensor = 'INSERT INTO "sensordatadb" (id, time,  router_id, slice_id, is_loss, delay, specific_type)  ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s)'

    _cursor_pool[0].execute("SELECT value FROM keyvalues where key = 'taskid'")
    task_id = _cursor_pool[0].fetchone()[0]
    _cursor_pool[0].execute("SELECT value FROM keyvalues where key = 'dataid'")
    data_id = _cursor_pool[0].fetchone()[0]
    start_time = time.perf_counter()
    test_net = Net()
    for router in test_net.core_routers.values():
        filename = "model_63_" + str(router.sign)
        router.agent.target_model = tf.keras.models.load_model(f"../resource/{filename}")
    test_net.initialize()
    paths = test_net.chose_paths()
    test_task_set, task_id, data_id = build_task_set(200, paths, _task_id=task_id, _data_id=data_id)
    for total_epoch in range(1000):
        print(f"第{total_epoch}轮")
        for j in range(50):
            task = test_task_set.pop()
            if isinstance(task, communicationtask.CommunicationTask):
                test_net.core_routers[task.path[0]].put_task(task)
            elif isinstance(task, sensortask.SensorTask):
                if task.path[0] == 0:
                    random.choice(list(test_net.edge_routers_first.values())).put_task(task)
                else:
                    random.choice(list(test_net.edge_routers_second.values())).put_task(task)
            else:
                random_index = choose_router_index_by_calculate_weight(_net=test_net)
                test_net.core_routers[random_index].put_task(task)
                # random.choice(list(test_net.core_routers.values())).put_task(task)
            if j == 25:
                test_net.deal_data()
        for router in test_net.core_routers.values():
            router.markov(is_test=True, is_best=True)
        """改变链路的带宽资源分配情况"""
        test_net.act_in_links()
        """处理上一个状态遗留下来的数据，并且利用动作更新分配标准"""
        test_net.deal_data()
        """选择通信链路的任务路径"""
        paths = test_net.chose_paths()
        tem_set, task_id, data_id = build_task_set(50, paths, _task_id=task_id, _data_id=data_id)
        test_task_set |= tem_set
        del tem_set
        print(time.perf_counter() - start_time)
        memory_usage = psutil.virtual_memory()
        print(f"Memory Usage: {memory_usage.percent}%")
        if memory_usage.percent >= 80:
            for router in test_net.core_routers.values():
                registration_db(_sql_communication, router.communication_values, _conn_in_train,
                                random.choice(_cursor_pool))
                router.communication_values.clear()
                registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
                router.calculate_values.clear()
                registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
                router.sensor_values.clear()
    """全部结束后的统一信息存储"""
    for router in test_net.core_routers.values():
        registration_db(_sql_communication, router.communication_values, _conn_in_train, random.choice(_cursor_pool))
        router.communication_values.clear()
        registration_db(_sql_calculate, router.calculate_values, _conn_in_train, random.choice(_cursor_pool))
        router.calculate_values.clear()
        registration_db(_sql_sensor, router.sensor_values, _conn_in_train, random.choice(_cursor_pool))
        router.sensor_values.clear()
    _cursor_pool[0].execute(_update_keyvalue_task, (task_id,))
    _cursor_pool[0].execute(_update_keyvalue_data, (data_id,))
    _conn_in_train.commit()
    print(time.perf_counter() - start_time)
