import random

import numpy as np

values = [1, 2, 3, 4, 5, 6, 7, 8]


def generate_sequence():
    _list_1 = []
    _weights = [3, 4, 60, 130, 200, 3000, 6000, 15000]
    while True:
        random_elements = random.choices(values, weights=_weights, k=3)
        if sum(random_elements) == 10:
            _list_1.append(random_elements)
        if len(_list_1) == 80:
            break
    return _list_1


if __name__ == '__main__':
    list_1 = generate_sequence()
    probability = np.zeros((3, 8))
    for element in list_1:
        probability[0][element[0] - 1] += 1
        probability[1][element[1] - 1] += 1
        probability[2][element[2] - 1] += 1
    print(probability)
