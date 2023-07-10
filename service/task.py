from abc import ABC, abstractmethod
from typing import List


class Task(ABC):
    def __init__(self, slice_sign):
        self.task_id = None
        self.data_id = None
        self.type = None
        """存储属于该任务的数据包"""
        self.dataset: List = []
        self.slice_id = slice_sign

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def set_property(self, *args):
        pass
