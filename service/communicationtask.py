import random
from typing import Union, List

from net_related.data import DataFactory, TypeOfData
from task import Task


class CommunicationTask(Task):
    def __init__(self, slice_sign: int, task_id: int, data_id: int,
                 communication_required: int = random.randint(3, 15), path: Union[List[int], None] = None):
        super().__init__(slice_sign)
        """这个任务的所有数据包的路径"""
        self.type = "CommunicationTask"
        self.task_id = task_id
        self.task_id += 1
        self.path = path
        self.communication_required: int = communication_required
        self.data_id = data_id
        for i in range(self.communication_required):
            data = DataFactory.create_data(TypeOfData.communication_data,
                                           slice_sign=slice_sign, dataid=self.data_id, path=path)
            """向self.dataset中添加数据包，为转发做准备"""
            self.dataset.append(data)
            """数据包序号递增"""
            self.data_id += 1

    def __repr__(self):
        return f"CommunicationTask,要求的通信资源为:{self.communication_required}"

    def __str__(self):
        return f"CommunicationTask,要求的通信资源为:{self.communication_required}"

    def set_property(self, *args):
        pass
