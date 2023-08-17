from abc import ABC, abstractmethod
from typing import List, Union


class Task(ABC):
    def __init__(self, slice_sign, path: Union[List[int], None] = None):
        self.task_id = None
        self.data_id = None
        self.type = None
        """存储属于该任务的数据包"""
        self.dataset: List = []
        self.slice_id = slice_sign
        self.path = path

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def set_property(self, *args):
        pass
