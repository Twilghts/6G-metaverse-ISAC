import random
from typing import List

import psycopg2

from data import DataFactory, TypeOfData
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


class CalculateTask(Task):
    def __init__(self, slice_sign: int, calculate_required: int = random.randint(1, 6)):
        super().__init__(slice_sign)
        """查询最新的taskid并将其赋值给这个任务的id"""
        _cursor.execute("SELECT value FROM keyvalues WHERE key = 'taskid'")
        self.sign = _cursor.fetchone()[0]

        """更新taskid的值，以便下次使用"""
        _cursor.execute("UPDATE keyvalues "
                        "SET value = (value + 1)"
                        "WHERE key = 'taskid'")

        """向表Task中注册该任务"""
        values = (self.sign, slice_sign, "CalculateTask")
        _cursor.execute(_sql_for_task, values)

        self.calculate_required: int = calculate_required

        """存储属于该任务的数据包"""
        self.dataset: List = []

        """查询最新的dataid并将其给data赋值"""
        _cursor.execute("SELECT value FROM keyvalues WHERE key = 'dataid'")
        data_sign = _cursor.fetchone()[0]

        for i in range(self.calculate_required):
            data = DataFactory.create_data(TypeOfData.calculate_data, slice_sign=slice_sign, dataid=data_sign)

            """向表data中注册该数据包"""
            values = (data.sign, slice_sign, "CalculateData")
            _cursor.execute(_sql_for_data, values)

            """向self.dataset中添加数据包，为转发做准备"""
            self.dataset.append(data)

            """向表task_data中插入数据"""
            values = (self.sign, data.sign)
            _cursor.execute(_sql_for_task_data, values)

            """数据包序号递增"""
            data_sign += 1

        """更新data最新的id"""
        data = (data_sign, )
        _cursor.execute(_update_keyvalue, data)

    def __repr__(self):
        return f"CalculateTask,要求的计算资源为:{self.calculate_required}"

    def __str__(self):
        return f"CalculateTask,要求的计算资源为:{self.calculate_required}"

    def set_property(self, *args):
        pass
