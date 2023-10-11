import random

from net_related.data import DataFactory, TypeOfData
from task import Task


class SensorTask(Task):
    def __init__(self, slice_sign: int, task_id: int, data_id: int, sensor_required: int = random.randint(15, 40),
                 path=None, specific_type=random.randint(1, 2)):
        super().__init__(slice_sign)
        self.type = "SensorTask"
        self.sensor_required: int = sensor_required
        self.task_id = task_id
        self.task_id += 1
        self.data_id = data_id
        self.path = path
        self.specific_type = specific_type
        for _ in range(self.sensor_required):
            data = DataFactory.create_data(TypeOfData.sensor_data, slice_sign=slice_sign,
                                           dataid=self.data_id, specific_type=specific_type, path=path, task_id=task_id)
            """向self.dataset中添加数据包，为转发做准备"""
            self.dataset.append(data)
            """数据包序号递增"""
            self.data_id += 1

    def __repr__(self):
        return f"SensorTask,要求的感知资源为:{self.sensor_required}"

    def __str__(self):
        return f"SensorTask,要求的感知资源为:{self.sensor_required}"
