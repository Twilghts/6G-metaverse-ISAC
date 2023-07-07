from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, slice_sign):
        self.slice_id = slice_sign

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def set_property(self, *args):
        pass
