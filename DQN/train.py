import random
from time import sleep
from typing import Set

from net_related.net import Net
from service.servicefactory import TaskFactory, TypeOfTask
from service.task import Task


def build_task_set(number: int) -> Set[Task]:
    _task_set = set()
    objects = {
        1: TypeOfTask.communication_task,
        2: TypeOfTask.calculate_task,
        3: TypeOfTask.sensor_task
    }
    for i in range(number):
        _random_number = random.randint(1, 3)
        _task_set.add(TaskFactory.create_task(objects[_random_number], slice_sign=random_slice(_random_number)))
    return _task_set


def random_slice(number: int):
    random_numbers = [1, 2, 3]
    random_numbers.remove(number)
    if random.random() < 0.7:
        return number
    else:
        return random.choice(random_numbers)


if __name__ == '__main__':
    task_set = build_task_set(1000)
    net = Net()
    sleep(1)
