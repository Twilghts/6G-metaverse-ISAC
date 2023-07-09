import random
import time
from typing import Set, Dict, List, Union

import psutil

import communicationtask
from net_related.net import Net
from service.servicefactory import TaskFactory, TypeOfTask
from service.task import Task


def build_task_set(number: int, _paths: Dict[int, List[List[int]]]) -> Set[Task]:
    _task_set = set()
    objects = {
        1: TypeOfTask.communication_task,
        2: TypeOfTask.calculate_task,
        3: TypeOfTask.sensor_task
    }
    path = None
    for _i in range(number):
        _random_number = random.randint(1, 3)
        _slice_number = random_slice(_random_number)
        if _random_number == 1:
            path: Union[List[int], None] = random.choice(_paths[_slice_number])
        _task_set.add(TaskFactory.create_task(objects[_random_number], slice_sign=_slice_number, path=path))
    return _task_set


def random_slice(number: int):
    random_numbers = [1, 2, 3]
    random_numbers.remove(number)
    if random.random() < 0.7:
        return number
    else:
        return random.choice(random_numbers)


if __name__ == '__main__':
    start_time = time.perf_counter()
    net = Net()
    net.initialize()
    paths = net.chose_paths()
    task_set = build_task_set(200, paths)
    """准备数据"""
    for i in range(170):
        for j in range(50):
            task = task_set.pop()
            if isinstance(task, communicationtask.CommunicationTask):
                net.routers[task.path[0]].put_task(task)
            else:
                random.choice(list(net.routers.values())).put_task(task)
            if j == 25:
                net.deal_data()
        for router in net.routers.values():
            router.markov()
        paths = net.chose_paths()
        task_set |= build_task_set(50, paths)

    print(f"准备工作消耗时间:{time.perf_counter() - start_time}")
    for total_epoch in range(1000):
        print(f"第{total_epoch}轮")
        for router in net.routers.values():
            router.agent.build_dataset()
        for router in net.routers.values():
            router.agent.replay()
        for i in range(75):
            for j in range(50):
                task = task_set.pop()
                if isinstance(task, communicationtask.CommunicationTask):
                    net.routers[task.path[0]].put_task(task)
                else:
                    random.choice(list(net.routers.values())).put_task(task)
                if j == 25:
                    net.deal_data()
            for router in net.routers.values():
                router.markov()
            task_set |= build_task_set(75, paths)

        print(time.perf_counter() - start_time)
        memory_usage = psutil.virtual_memory()
        print(f"Memory Usage: {memory_usage.percent}%")
