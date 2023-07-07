from service.servicefactory import TaskFactory, TypeOfTask

if __name__ == '__main__':
    for i in range(10000):
        task_1 = TaskFactory.create_task(task_type=TypeOfTask.sensor_task, slice_sign=1)
        task_2 = TaskFactory.create_task(task_type=TypeOfTask.communication_task, slice_sign=2)
        task_3 = TaskFactory.create_task(task_type=TypeOfTask.calculate_task, slice_sign=3)
        print(task_1)
        print(task_2)
        print(task_3)
        print(f"第{i}轮")

