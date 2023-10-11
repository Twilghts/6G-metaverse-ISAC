import random

from data import DataFactory, TypeOfData
from task import Task


class CalculateTask(Task):
    def __init__(self, slice_sign: int, task_id: int, data_id: int,
                 calculate_required: int = random.randint(1, 6)):
        super().__init__(slice_sign)
        self.type = "CalculateTask"
        self.calculate_required: int = calculate_required
        self.task_id = task_id
        self.task_id += 1
        self.data_id = data_id
        for _ in range(self.calculate_required):
            data = DataFactory.create_data(TypeOfData.calculate_data, slice_sign=slice_sign, dataid=self.data_id,
                                           task_id=task_id)
            """向self.dataset中添加数据包，为转发做准备"""
            self.dataset.append(data)
            """数据包序号递增"""
            self.data_id += 1

    def __repr__(self):
        return f"CalculateTask,要求的计算资源为:{self.calculate_required}"

    def __str__(self):
        return f"CalculateTask,要求的计算资源为:{self.calculate_required}"
