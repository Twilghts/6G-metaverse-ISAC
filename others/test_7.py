import queue
import multiprocessing
import random

import numpy as np

values = [1, 2, 3, 4, 5, 6, 7, 8]


def generate_sequence(queue_result):
    _list_1 = []
    _weights = [5, 13, 31, 60, 200, 500, 1000, 3000]
    while True:
        random_elements = random.choices(values, weights=_weights, k=3)
        if sum(random_elements) == 10:
            _list_1.append(random_elements)
        if len(_list_1) == 100:
            break
    queue_result.put(_list_1)


if __name__ == '__main__':
    list_1 = []
    result_queue = queue = multiprocessing.Queue()
    process_pool = []
    for i in range(10):
        my_process = multiprocessing.Process(target=generate_sequence, args=(result_queue, ))
        process_pool.append(my_process)
        my_process.start()
    for process in process_pool:
        process.join()
    while not result_queue.empty():
        list_1.extend(result_queue.get())
    probability = np.zeros((3, 8))
    for element in list_1:
        probability[0][element[0] - 1] += 1
        probability[1][element[1] - 1] += 1
        probability[2][element[2] - 1] += 1
    print(probability)
