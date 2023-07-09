from time import sleep

import sensortask
from service.servicefactory import TaskFactory, TypeOfTask
from service.sensortask import SensorTask
from service.task import Task

if __name__ == '__main__':
    task = TaskFactory.create_task(TypeOfTask.sensor_task, 1)
    print(task)
    print(isinstance(task, SensorTask))
    sleep(1)
    print(SensorTask.__class__.__name__)
    print(task.__class__.__name__)
    print(isinstance(1, int))
    print(isinstance(task, Task))
    print(type(task))
    print(isinstance(task, sensortask.SensorTask))
