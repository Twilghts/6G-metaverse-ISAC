import numpy as np

if __name__ == '__main__':
    x = np.random.random((3, 3))
    y = x.reshape(1, 9)
    z = [*y]
    h = y[0]
    w = [*h]
    r = y[:, 0:9]
    states = np.random.random((9, 9))
    states_2 = []
    for i in range(9):
        states_2.append(np.random.random((1, 9)))

