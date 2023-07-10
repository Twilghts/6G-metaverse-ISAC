from typing import Union, List

from sensortask import SensorTask
from calculatetask import CalculateTask
from communicationtask import CommunicationTask
from task import Task

from enum import Enum


class TypeOfTask(Enum):
    sensor_task = SensorTask
    calculate_task = CalculateTask
    communication_task = CommunicationTask


class TaskFactory:
    @staticmethod
    def create_task(task_type: TypeOfTask, slice_sign: int, task_id: int, data_id: int,
                    path: Union[List[int], None] = None) -> Task:
        if task_type == TypeOfTask.communication_task:
            return CommunicationTask(slice_sign=slice_sign, path=path, task_id=task_id, data_id=data_id)
        elif task_type == TypeOfTask.calculate_task:
            return CalculateTask(slice_sign=slice_sign, task_id=task_id, data_id=data_id)
        elif task_type == TypeOfTask.sensor_task:
            return SensorTask(slice_sign=slice_sign, task_id=task_id, data_id=data_id)
