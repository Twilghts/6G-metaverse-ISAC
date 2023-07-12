import random
from typing import List

import psycopg2

from net_related.data import DataFactory, TypeOfData
from task import Task

_conn_with_task = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="rkw2536153"
)
_cursor = _conn_with_task.cursor()
_sql_for_task = 'INSERT INTO task (id, slice, type)  ' \
                'VALUES (%s, %s, %s)'

_sql_for_task_data = 'INSERT INTO taskdata (taskid, dataid)  ' \
                     'VALUES (%s, %s)'

_update_keyvalue = "UPDATE keyvalues SET value = %s WHERE key = 'dataid'"

_sql_for_data = 'INSERT INTO data (id, slice, type)  ' \
                'VALUES (%s, %s, %s)'


def registration_db(sign: int, slice_sign: int, dataset: List, conn):
    cursor = conn.cursor()
    """向表Task中注册该任务"""
    values = (sign, slice_sign, "SensorTask")
    cursor.execute(_sql_for_task, values)
    """存储属于该任务的数据包"""
    values_data = []
    values_taskdata = []
    for data in dataset:
        """向表data中注册该数据包"""
        value_data = (data.sign, slice_sign, "SensorTask")
        values_data.append(value_data)
        """向表task_data中插入数据"""
        value_taskdata = (sign, data.sign)
        values_taskdata.append(value_taskdata)
    cursor.executemany(_sql_for_data, values_data)
    cursor.executemany(_sql_for_task_data, values_taskdata)
    conn.commit()
    cursor.close()


class SensorTask(Task):
    def __init__(self, slice_sign: int, task_id: int, data_id: int,
                 sensor_required: int = random.randint(15, 40)):
        super().__init__(slice_sign)
        self.type = "SensorTask"
        self.sensor_required: int = sensor_required
        self.task_id = task_id
        self.task_id += 1
        self.data_id = data_id
        for i in range(self.sensor_required):
            data = DataFactory.create_data(TypeOfData.sensor_data, slice_sign=slice_sign, dataid=self.data_id)
            """向self.dataset中添加数据包，为转发做准备"""
            self.dataset.append(data)
            """数据包序号递增"""
            self.data_id += 1
        # """查询最新的taskid并将其赋值给这个任务的id"""
        # _cursor.execute("SELECT value FROM keyvalues WHERE key = 'taskid'")
        # self.sign = _cursor.fetchone()[0]
        # """查询最新的dataid并将其给data赋值"""
        # _cursor.execute("SELECT value FROM keyvalues WHERE key = 'dataid'")
        # data_sign = _cursor.fetchone()[0]

        # process = threading.Thread(target=registration_db, args=(self.sign, slice_sign,
        #                                                          self.dataset, _conn_in_train))
        # process.start()
        # """更新taskid的值，以便下次使用"""
        # _cursor.execute("UPDATE keyvalues "
        #                 "SET value = (value + 1)"
        #                 "WHERE key = 'taskid'")
        # _cursor.execute(_update_keyvalue, (data_sign,))
        # _conn_in_train.commit()

    def __repr__(self):
        return f"SensorTask,要求的感知资源为:{self.sensor_required}"

    def __str__(self):
        return f"SensorTask,要求的感知资源为:{self.sensor_required}"

    def set_property(self, *args):
        pass
