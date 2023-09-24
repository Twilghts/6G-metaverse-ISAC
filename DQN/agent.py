# -*- coding: utf-8 -*-

import random
from collections import namedtuple, deque
from typing import List

import numpy as np
import tensorflow as tf

######################################################################
# Replay Memory(回放缓存大小)
_capacity = 2500
_transition = namedtuple('_transition', ('state', 'action_index', 'next_state', 'reward'))
_epochs = 3


class ReplyMemory(object):

    def __init__(self):
        self.memory: deque = deque([], maxlen=_capacity)

    def push(self, *args):
        # log = []
        # # *args一般共有4个元素，第一个state是1*9的ndarray，
        # # 第二个是action，是一个数字，第三个是reward，是一个浮点数，
        # # 第四个是next_state，是一个1*9的ndarray。
        # for arg in args:
        #     if isinstance(arg, Iterable):
        #         log.extend(arg[0])
        #     else:
        #         log.append(arg)
        # self.memory.append(log)
        self.memory.append(_transition(*args))

    def sample(self, batch_size) -> list:
        return random.sample(self.memory, batch_size)

    def __len__(self) -> int:
        return len(self.memory)


######################################################################
# DQN algorithm
def action_area():
    return [[[0.2, 0.7, 0.1], [0.2, 0.4, 0.4], [0.2, 0.3, 0.5]],
            [[0.7, 0.1, 0.2], [0.2, 0.6, 0.2], [0.2, 0.4, 0.4]],
            [[0.1, 0.4, 0.5], [0.1, 0.1, 0.8], [0.1, 0.7, 0.2]],
            [[0.1, 0.2, 0.7], [0.3, 0.1, 0.6], [0.5, 0.2, 0.3]],
            [[0.3, 0.5, 0.2], [0.1, 0.4, 0.5], [0.7, 0.1, 0.2]],
            [[0.6, 0.2, 0.2], [0.7, 0.1, 0.2], [0.4, 0.3, 0.3]],
            [[0.3, 0.6, 0.1], [0.1, 0.6, 0.3], [0.4, 0.3, 0.3]],
            [[0.1, 0.1, 0.8], [0.5, 0.3, 0.2], [0.2, 0.7, 0.1]],
            [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.6, 0.2, 0.2]],
            [[0.1, 0.3, 0.6], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
            [[0.4, 0.1, 0.5], [0.6, 0.1, 0.3], [0.2, 0.3, 0.5]],
            [[0.6, 0.1, 0.3], [0.4, 0.4, 0.2], [0.3, 0.1, 0.6]],
            [[0.4, 0.4, 0.2], [0.3, 0.6, 0.1], [0.4, 0.3, 0.3]],
            [[0.1, 0.3, 0.6], [0.4, 0.3, 0.3], [0.3, 0.4, 0.3]],
            [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
            [[0.1, 0.3, 0.6], [0.7, 0.1, 0.2], [0.5, 0.4, 0.1]],
            [[0.1, 0.6, 0.3], [0.6, 0.1, 0.3], [0.5, 0.3, 0.2]],
            [[0.3, 0.4, 0.3], [0.2, 0.4, 0.4], [0.2, 0.1, 0.7]],
            [[0.2, 0.4, 0.4], [0.3, 0.4, 0.3], [0.2, 0.6, 0.2]],
            [[0.4, 0.2, 0.4], [0.7, 0.1, 0.2], [0.3, 0.5, 0.2]],
            [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.3, 0.5, 0.2]],
            [[0.3, 0.3, 0.4], [0.6, 0.2, 0.2], [0.1, 0.1, 0.8]],
            [[0.4, 0.2, 0.4], [0.2, 0.5, 0.3], [0.2, 0.6, 0.2]],
            [[0.3, 0.6, 0.1], [0.1, 0.3, 0.6], [0.1, 0.2, 0.7]],
            [[0.1, 0.2, 0.7], [0.8, 0.1, 0.1], [0.2, 0.1, 0.7]],
            [[0.1, 0.1, 0.8], [0.3, 0.5, 0.2], [0.3, 0.4, 0.3]],
            [[0.2, 0.7, 0.1], [0.4, 0.5, 0.1], [0.1, 0.4, 0.5]],
            [[0.6, 0.1, 0.3], [0.1, 0.7, 0.2], [0.8, 0.1, 0.1]],
            [[0.2, 0.6, 0.2], [0.2, 0.1, 0.7], [0.4, 0.1, 0.5]],
            [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.1, 0.2, 0.7]],
            [[0.4, 0.3, 0.3], [0.6, 0.3, 0.1], [0.1, 0.3, 0.6]],
            [[0.1, 0.1, 0.8], [0.2, 0.1, 0.7], [0.3, 0.1, 0.6]],
            [[0.1, 0.8, 0.1], [0.5, 0.2, 0.3], [0.3, 0.5, 0.2]],
            [[0.3, 0.2, 0.5], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
            [[0.1, 0.4, 0.5], [0.5, 0.3, 0.2], [0.5, 0.1, 0.4]],
            [[0.3, 0.1, 0.6], [0.5, 0.4, 0.1], [0.1, 0.5, 0.4]],
            [[0.7, 0.2, 0.1], [0.2, 0.1, 0.7], [0.1, 0.1, 0.8]],
            [[0.2, 0.6, 0.2], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
            [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]],
            [[0.4, 0.4, 0.2], [0.5, 0.2, 0.3], [0.1, 0.6, 0.3]],
            [[0.3, 0.3, 0.4], [0.5, 0.1, 0.4], [0.6, 0.1, 0.3]],
            [[0.2, 0.4, 0.4], [0.1, 0.5, 0.4], [0.2, 0.1, 0.7]],
            [[0.3, 0.1, 0.6], [0.1, 0.7, 0.2], [0.4, 0.2, 0.4]],
            [[0.3, 0.3, 0.4], [0.1, 0.3, 0.6], [0.3, 0.2, 0.5]],
            [[0.1, 0.6, 0.3], [0.6, 0.3, 0.1], [0.3, 0.1, 0.6]],
            [[0.3, 0.5, 0.2], [0.4, 0.5, 0.1], [0.6, 0.3, 0.1]],
            [[0.4, 0.3, 0.3], [0.1, 0.4, 0.5], [0.1, 0.6, 0.3]],
            [[0.5, 0.4, 0.1], [0.2, 0.2, 0.6], [0.3, 0.2, 0.5]],
            [[0.3, 0.6, 0.1], [0.4, 0.3, 0.3], [0.5, 0.2, 0.3]],
            [[0.3, 0.5, 0.2], [0.2, 0.2, 0.6], [0.4, 0.2, 0.4]],
            [[0.8, 0.1, 0.1], [0.1, 0.6, 0.3], [0.1, 0.1, 0.8]],
            [[0.1, 0.8, 0.1], [0.1, 0.5, 0.4], [0.3, 0.6, 0.1]],
            [[0.1, 0.2, 0.7], [0.2, 0.7, 0.1], [0.2, 0.6, 0.2]],
            [[0.3, 0.5, 0.2], [0.4, 0.1, 0.5], [0.4, 0.5, 0.1]],
            [[0.3, 0.6, 0.1], [0.5, 0.4, 0.1], [0.4, 0.1, 0.5]],
            [[0.4, 0.4, 0.2], [0.3, 0.1, 0.6], [0.3, 0.4, 0.3]],
            [[0.1, 0.7, 0.2], [0.3, 0.4, 0.3], [0.5, 0.1, 0.4]],
            [[0.6, 0.1, 0.3], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1]],
            [[0.8, 0.1, 0.1], [0.1, 0.3, 0.6], [0.2, 0.5, 0.3]],
            [[0.1, 0.2, 0.7], [0.3, 0.4, 0.3], [0.1, 0.8, 0.1]],
            [[0.2, 0.4, 0.4], [0.1, 0.7, 0.2], [0.1, 0.5, 0.4]],
            [[0.4, 0.5, 0.1], [0.5, 0.3, 0.2], [0.1, 0.2, 0.7]],
            [[0.3, 0.5, 0.2], [0.1, 0.3, 0.6], [0.5, 0.4, 0.1]],
            [[0.8, 0.1, 0.1], [0.4, 0.4, 0.2], [0.5, 0.4, 0.1]],
            [[0.7, 0.2, 0.1], [0.8, 0.1, 0.1], [0.5, 0.3, 0.2]],
            [[0.7, 0.1, 0.2], [0.2, 0.1, 0.7], [0.6, 0.1, 0.3]],
            [[0.3, 0.6, 0.1], [0.2, 0.4, 0.4], [0.1, 0.2, 0.7]],
            [[0.2, 0.3, 0.5], [0.2, 0.5, 0.3], [0.1, 0.2, 0.7]],
            [[0.2, 0.4, 0.4], [0.5, 0.4, 0.1], [0.2, 0.7, 0.1]],
            [[0.7, 0.1, 0.2], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
            [[0.3, 0.1, 0.6], [0.2, 0.2, 0.6], [0.1, 0.8, 0.1]],
            [[0.2, 0.4, 0.4], [0.3, 0.4, 0.3], [0.2, 0.7, 0.1]],
            [[0.1, 0.8, 0.1], [0.7, 0.2, 0.1], [0.2, 0.4, 0.4]],
            [[0.5, 0.2, 0.3], [0.2, 0.3, 0.5], [0.1, 0.5, 0.4]],
            [[0.2, 0.1, 0.7], [0.3, 0.5, 0.2], [0.2, 0.5, 0.3]],
            [[0.1, 0.6, 0.3], [0.6, 0.1, 0.3], [0.1, 0.7, 0.2]],
            [[0.3, 0.3, 0.4], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
            [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.2, 0.5, 0.3]],
            [[0.4, 0.4, 0.2], [0.1, 0.6, 0.3], [0.6, 0.2, 0.2]],
            [[0.4, 0.2, 0.4], [0.1, 0.3, 0.6], [0.2, 0.7, 0.1]],
            [[0.2, 0.1, 0.7], [0.2, 0.3, 0.5], [0.4, 0.3, 0.3]],
            [[0.1, 0.1, 0.8], [0.1, 0.3, 0.6], [0.6, 0.2, 0.2]],
            [[0.5, 0.4, 0.1], [0.2, 0.5, 0.3], [0.2, 0.7, 0.1]],
            [[0.2, 0.5, 0.3], [0.5, 0.2, 0.3], [0.1, 0.6, 0.3]],
            [[0.2, 0.5, 0.3], [0.3, 0.6, 0.1], [0.7, 0.2, 0.1]],
            [[0.5, 0.4, 0.1], [0.2, 0.1, 0.7], [0.4, 0.4, 0.2]],
            [[0.1, 0.1, 0.8], [0.4, 0.2, 0.4], [0.1, 0.4, 0.5]],
            [[0.1, 0.2, 0.7], [0.6, 0.1, 0.3], [0.1, 0.5, 0.4]],
            [[0.2, 0.2, 0.6], [0.4, 0.3, 0.3], [0.1, 0.4, 0.5]],
            [[0.2, 0.4, 0.4], [0.3, 0.6, 0.1], [0.1, 0.2, 0.7]],
            [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.7, 0.2, 0.1]],
            [[0.8, 0.1, 0.1], [0.1, 0.1, 0.8], [0.1, 0.5, 0.4]],
            [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.1, 0.5, 0.4]],
            [[0.1, 0.1, 0.8], [0.2, 0.1, 0.7], [0.6, 0.2, 0.2]],
            [[0.6, 0.1, 0.3], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
            [[0.1, 0.7, 0.2], [0.3, 0.6, 0.1], [0.1, 0.4, 0.5]],
            [[0.2, 0.5, 0.3], [0.3, 0.1, 0.6], [0.4, 0.1, 0.5]],
            [[0.8, 0.1, 0.1], [0.3, 0.4, 0.3], [0.2, 0.1, 0.7]],
            [[0.1, 0.7, 0.2], [0.3, 0.4, 0.3], [0.3, 0.2, 0.5]],
            [[0.1, 0.4, 0.5], [0.2, 0.6, 0.2], [0.1, 0.5, 0.4]],
            [[0.1, 0.1, 0.8], [0.6, 0.2, 0.2], [0.1, 0.3, 0.6]],
            [[0.5, 0.1, 0.4], [0.1, 0.6, 0.3], [0.6, 0.2, 0.2]],
            [[0.8, 0.1, 0.1], [0.5, 0.4, 0.1], [0.7, 0.2, 0.1]],
            [[0.8, 0.1, 0.1], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
            [[0.1, 0.2, 0.7], [0.5, 0.1, 0.4], [0.5, 0.2, 0.3]],
            [[0.5, 0.2, 0.3], [0.6, 0.2, 0.2], [0.2, 0.3, 0.5]],
            [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.3, 0.6, 0.1]],
            [[0.6, 0.3, 0.1], [0.2, 0.2, 0.6], [0.1, 0.7, 0.2]],
            [[0.2, 0.1, 0.7], [0.1, 0.1, 0.8], [0.2, 0.3, 0.5]],
            [[0.2, 0.4, 0.4], [0.2, 0.1, 0.7], [0.3, 0.3, 0.4]],
            [[0.4, 0.5, 0.1], [0.6, 0.1, 0.3], [0.8, 0.1, 0.1]],
            [[0.3, 0.6, 0.1], [0.1, 0.4, 0.5], [0.4, 0.2, 0.4]],
            [[0.6, 0.1, 0.3], [0.8, 0.1, 0.1], [0.2, 0.1, 0.7]],
            [[0.3, 0.6, 0.1], [0.3, 0.2, 0.5], [0.1, 0.1, 0.8]],
            [[0.6, 0.2, 0.2], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3]],
            [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.1, 0.5, 0.4]],
            [[0.6, 0.2, 0.2], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
            [[0.2, 0.6, 0.2], [0.3, 0.1, 0.6], [0.1, 0.5, 0.4]],
            [[0.5, 0.4, 0.1], [0.1, 0.2, 0.7], [0.4, 0.1, 0.5]],
            [[0.2, 0.6, 0.2], [0.5, 0.4, 0.1], [0.4, 0.5, 0.1]],
            [[0.5, 0.4, 0.1], [0.6, 0.1, 0.3], [0.3, 0.4, 0.3]],
            [[0.1, 0.8, 0.1], [0.5, 0.3, 0.2], [0.1, 0.6, 0.3]],
            [[0.7, 0.2, 0.1], [0.6, 0.3, 0.1], [0.5, 0.2, 0.3]],
            [[0.4, 0.5, 0.1], [0.3, 0.4, 0.3], [0.1, 0.6, 0.3]],
            [[0.3, 0.3, 0.4], [0.6, 0.3, 0.1], [0.2, 0.1, 0.7]],
            [[0.2, 0.7, 0.1], [0.1, 0.1, 0.8], [0.5, 0.4, 0.1]],
            [[0.2, 0.6, 0.2], [0.4, 0.1, 0.5], [0.7, 0.2, 0.1]],
            [[0.1, 0.1, 0.8], [0.1, 0.3, 0.6], [0.3, 0.3, 0.4]],
            [[0.5, 0.2, 0.3], [0.1, 0.8, 0.1], [0.3, 0.1, 0.6]],
            [[0.2, 0.6, 0.2], [0.5, 0.4, 0.1], [0.6, 0.2, 0.2]],
            [[0.3, 0.4, 0.3], [0.1, 0.8, 0.1], [0.1, 0.2, 0.7]],
            [[0.4, 0.3, 0.3], [0.3, 0.5, 0.2], [0.2, 0.1, 0.7]],
            [[0.1, 0.4, 0.5], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
            [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.2, 0.7, 0.1]],
            [[0.7, 0.1, 0.2], [0.3, 0.6, 0.1], [0.1, 0.8, 0.1]],
            [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.1, 0.8, 0.1]],
            [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.1, 0.7, 0.2]],
            [[0.5, 0.1, 0.4], [0.4, 0.3, 0.3], [0.2, 0.3, 0.5]],
            [[0.7, 0.1, 0.2], [0.8, 0.1, 0.1], [0.6, 0.3, 0.1]],
            [[0.7, 0.2, 0.1], [0.4, 0.1, 0.5], [0.2, 0.7, 0.1]],
            [[0.4, 0.4, 0.2], [0.2, 0.3, 0.5], [0.2, 0.4, 0.4]],
            [[0.1, 0.6, 0.3], [0.1, 0.1, 0.8], [0.3, 0.2, 0.5]],
            [[0.1, 0.4, 0.5], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
            [[0.2, 0.1, 0.7], [0.4, 0.1, 0.5], [0.7, 0.2, 0.1]],
            [[0.4, 0.2, 0.4], [0.1, 0.6, 0.3], [0.2, 0.6, 0.2]],
            [[0.1, 0.1, 0.8], [0.6, 0.3, 0.1], [0.2, 0.5, 0.3]],
            [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.3, 0.6, 0.1]],
            [[0.5, 0.2, 0.3], [0.4, 0.3, 0.3], [0.1, 0.2, 0.7]],
            [[0.1, 0.4, 0.5], [0.7, 0.2, 0.1], [0.3, 0.6, 0.1]],
            [[0.4, 0.2, 0.4], [0.3, 0.5, 0.2], [0.7, 0.2, 0.1]],
            [[0.3, 0.4, 0.3], [0.2, 0.6, 0.2], [0.1, 0.3, 0.6]],
            [[0.4, 0.3, 0.3], [0.4, 0.1, 0.5], [0.8, 0.1, 0.1]],
            [[0.1, 0.2, 0.7], [0.5, 0.1, 0.4], [0.2, 0.7, 0.1]],
            [[0.1, 0.5, 0.4], [0.3, 0.4, 0.3], [0.3, 0.6, 0.1]],
            [[0.1, 0.7, 0.2], [0.2, 0.7, 0.1], [0.1, 0.5, 0.4]],
            [[0.3, 0.5, 0.2], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
            [[0.3, 0.3, 0.4], [0.3, 0.1, 0.6], [0.4, 0.1, 0.5]],
            [[0.4, 0.3, 0.3], [0.2, 0.1, 0.7], [0.5, 0.4, 0.1]],
            [[0.2, 0.1, 0.7], [0.6, 0.2, 0.2], [0.2, 0.4, 0.4]],
            [[0.2, 0.3, 0.5], [0.1, 0.6, 0.3], [0.7, 0.1, 0.2]],
            [[0.2, 0.5, 0.3], [0.1, 0.2, 0.7], [0.3, 0.5, 0.2]],
            [[0.1, 0.3, 0.6], [0.6, 0.2, 0.2], [0.7, 0.2, 0.1]],
            [[0.3, 0.3, 0.4], [0.6, 0.1, 0.3], [0.4, 0.2, 0.4]],
            [[0.4, 0.1, 0.5], [0.2, 0.1, 0.7], [0.3, 0.1, 0.6]],
            [[0.1, 0.3, 0.6], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
            [[0.2, 0.5, 0.3], [0.2, 0.4, 0.4], [0.4, 0.3, 0.3]],
            [[0.7, 0.2, 0.1], [0.6, 0.2, 0.2], [0.2, 0.5, 0.3]],
            [[0.4, 0.4, 0.2], [0.4, 0.1, 0.5], [0.4, 0.5, 0.1]],
            [[0.3, 0.5, 0.2], [0.5, 0.3, 0.2], [0.5, 0.1, 0.4]],
            [[0.2, 0.3, 0.5], [0.7, 0.1, 0.2], [0.5, 0.4, 0.1]],
            [[0.7, 0.2, 0.1], [0.1, 0.4, 0.5], [0.3, 0.4, 0.3]],
            [[0.4, 0.2, 0.4], [0.7, 0.1, 0.2], [0.1, 0.1, 0.8]],
            [[0.8, 0.1, 0.1], [0.4, 0.5, 0.1], [0.2, 0.5, 0.3]],
            [[0.7, 0.2, 0.1], [0.2, 0.2, 0.6], [0.3, 0.1, 0.6]],
            [[0.3, 0.6, 0.1], [0.6, 0.3, 0.1], [0.2, 0.2, 0.6]],
            [[0.2, 0.7, 0.1], [0.2, 0.2, 0.6], [0.4, 0.2, 0.4]],
            [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.6, 0.2, 0.2]],
            [[0.6, 0.3, 0.1], [0.8, 0.1, 0.1], [0.1, 0.7, 0.2]],
            [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.1, 0.6, 0.3]],
            [[0.2, 0.2, 0.6], [0.6, 0.1, 0.3], [0.2, 0.4, 0.4]],
            [[0.6, 0.2, 0.2], [0.4, 0.4, 0.2], [0.5, 0.1, 0.4]],
            [[0.8, 0.1, 0.1], [0.2, 0.5, 0.3], [0.3, 0.6, 0.1]],
            [[0.1, 0.8, 0.1], [0.6, 0.3, 0.1], [0.4, 0.2, 0.4]],
            [[0.2, 0.5, 0.3], [0.3, 0.3, 0.4], [0.5, 0.4, 0.1]],
            [[0.4, 0.3, 0.3], [0.3, 0.6, 0.1], [0.2, 0.6, 0.2]],
            [[0.4, 0.5, 0.1], [0.6, 0.1, 0.3], [0.3, 0.4, 0.3]],
            [[0.3, 0.6, 0.1], [0.7, 0.1, 0.2], [0.2, 0.2, 0.6]],
            [[0.1, 0.5, 0.4], [0.4, 0.5, 0.1], [0.1, 0.3, 0.6]],
            [[0.5, 0.2, 0.3], [0.2, 0.5, 0.3], [0.1, 0.3, 0.6]],
            [[0.7, 0.1, 0.2], [0.7, 0.2, 0.1], [0.2, 0.1, 0.7]],
            [[0.2, 0.7, 0.1], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
            [[0.3, 0.3, 0.4], [0.4, 0.5, 0.1], [0.2, 0.7, 0.1]],
            [[0.3, 0.1, 0.6], [0.7, 0.1, 0.2], [0.2, 0.4, 0.4]],
            [[0.3, 0.4, 0.3], [0.4, 0.1, 0.5], [0.8, 0.1, 0.1]],
            [[0.5, 0.3, 0.2], [0.6, 0.3, 0.1], [0.3, 0.1, 0.6]],
            [[0.1, 0.7, 0.2], [0.7, 0.2, 0.1], [0.6, 0.2, 0.2]],
            [[0.2, 0.7, 0.1], [0.6, 0.1, 0.3], [0.6, 0.3, 0.1]],
            [[0.5, 0.4, 0.1], [0.5, 0.2, 0.3], [0.1, 0.1, 0.8]],
            [[0.2, 0.2, 0.6], [0.4, 0.2, 0.4], [0.3, 0.1, 0.6]],
            [[0.7, 0.1, 0.2], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
            [[0.1, 0.5, 0.4], [0.1, 0.3, 0.6], [0.3, 0.5, 0.2]],
            [[0.8, 0.1, 0.1], [0.5, 0.4, 0.1], [0.4, 0.4, 0.2]],
            [[0.8, 0.1, 0.1], [0.6, 0.1, 0.3], [0.5, 0.3, 0.2]],
            [[0.4, 0.3, 0.3], [0.2, 0.4, 0.4], [0.1, 0.6, 0.3]],
            [[0.2, 0.5, 0.3], [0.3, 0.2, 0.5], [0.1, 0.4, 0.5]],
            [[0.1, 0.8, 0.1], [0.1, 0.7, 0.2], [0.1, 0.6, 0.3]],
            [[0.2, 0.5, 0.3], [0.4, 0.1, 0.5], [0.2, 0.2, 0.6]],
            [[0.4, 0.2, 0.4], [0.6, 0.1, 0.3], [0.7, 0.1, 0.2]],
            [[0.5, 0.3, 0.2], [0.3, 0.1, 0.6], [0.6, 0.3, 0.1]],
            [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.2, 0.7, 0.1]],
            [[0.4, 0.2, 0.4], [0.3, 0.2, 0.5], [0.8, 0.1, 0.1]],
            [[0.4, 0.3, 0.3], [0.1, 0.4, 0.5], [0.4, 0.1, 0.5]],
            [[0.4, 0.4, 0.2], [0.7, 0.2, 0.1], [0.4, 0.1, 0.5]],
            [[0.1, 0.8, 0.1], [0.3, 0.4, 0.3], [0.5, 0.4, 0.1]],
            [[0.3, 0.3, 0.4], [0.1, 0.3, 0.6], [0.7, 0.1, 0.2]],
            [[0.4, 0.1, 0.5], [0.3, 0.3, 0.4], [0.2, 0.6, 0.2]],
            [[0.6, 0.2, 0.2], [0.1, 0.1, 0.8], [0.2, 0.3, 0.5]],
            [[0.2, 0.1, 0.7], [0.3, 0.1, 0.6], [0.7, 0.1, 0.2]],
            [[0.2, 0.3, 0.5], [0.6, 0.2, 0.2], [0.2, 0.1, 0.7]],
            [[0.2, 0.1, 0.7], [0.2, 0.7, 0.1], [0.2, 0.5, 0.3]],
            [[0.6, 0.2, 0.2], [0.4, 0.5, 0.1], [0.2, 0.6, 0.2]],
            [[0.5, 0.1, 0.4], [0.1, 0.7, 0.2], [0.3, 0.6, 0.1]],
            [[0.1, 0.6, 0.3], [0.2, 0.1, 0.7], [0.2, 0.7, 0.1]],
            [[0.1, 0.6, 0.3], [0.5, 0.4, 0.1], [0.7, 0.2, 0.1]],
            [[0.4, 0.5, 0.1], [0.6, 0.2, 0.2], [0.6, 0.1, 0.3]],
            [[0.2, 0.5, 0.3], [0.4, 0.4, 0.2], [0.5, 0.3, 0.2]],
            [[0.3, 0.1, 0.6], [0.3, 0.5, 0.2], [0.4, 0.1, 0.5]],
            [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.2, 0.1, 0.7]],
            [[0.3, 0.2, 0.5], [0.4, 0.4, 0.2], [0.5, 0.1, 0.4]],
            [[0.3, 0.2, 0.5], [0.1, 0.5, 0.4], [0.8, 0.1, 0.1]],
            [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.1, 0.6]],
            [[0.1, 0.6, 0.3], [0.5, 0.2, 0.3], [0.8, 0.1, 0.1]],
            [[0.4, 0.3, 0.3], [0.5, 0.1, 0.4], [0.2, 0.7, 0.1]],
            [[0.5, 0.3, 0.2], [0.3, 0.4, 0.3], [0.8, 0.1, 0.1]],
            [[0.1, 0.3, 0.6], [0.1, 0.8, 0.1], [0.1, 0.7, 0.2]],
            [[0.4, 0.5, 0.1], [0.1, 0.4, 0.5], [0.2, 0.4, 0.4]],
            [[0.3, 0.1, 0.6], [0.5, 0.4, 0.1], [0.4, 0.3, 0.3]],
            [[0.7, 0.2, 0.1], [0.2, 0.6, 0.2], [0.3, 0.2, 0.5]],
            [[0.2, 0.3, 0.5], [0.5, 0.4, 0.1], [0.6, 0.1, 0.3]],
            [[0.2, 0.7, 0.1], [0.1, 0.6, 0.3], [0.5, 0.2, 0.3]],
            [[0.1, 0.8, 0.1], [0.4, 0.4, 0.2], [0.7, 0.1, 0.2]],
            [[0.2, 0.5, 0.3], [0.6, 0.3, 0.1], [0.1, 0.2, 0.7]],
            [[0.1, 0.2, 0.7], [0.4, 0.5, 0.1], [0.5, 0.2, 0.3]],
            [[0.6, 0.1, 0.3], [0.1, 0.4, 0.5], [0.1, 0.8, 0.1]],
            [[0.1, 0.8, 0.1], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
            [[0.4, 0.3, 0.3], [0.2, 0.2, 0.6], [0.1, 0.8, 0.1]],
            [[0.3, 0.4, 0.3], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
            [[0.4, 0.5, 0.1], [0.4, 0.4, 0.2], [0.2, 0.5, 0.3]],
            [[0.4, 0.1, 0.5], [0.4, 0.4, 0.2], [0.1, 0.7, 0.2]],
            [[0.6, 0.1, 0.3], [0.5, 0.3, 0.2], [0.1, 0.6, 0.3]],
            [[0.5, 0.3, 0.2], [0.2, 0.7, 0.1], [0.3, 0.6, 0.1]],
            [[0.3, 0.3, 0.4], [0.2, 0.5, 0.3], [0.4, 0.4, 0.2]],
            [[0.1, 0.3, 0.6], [0.4, 0.3, 0.3], [0.1, 0.7, 0.2]],
            [[0.4, 0.4, 0.2], [0.2, 0.1, 0.7], [0.5, 0.4, 0.1]],
            [[0.2, 0.1, 0.7], [0.7, 0.2, 0.1], [0.5, 0.2, 0.3]],
            [[0.5, 0.3, 0.2], [0.5, 0.4, 0.1], [0.7, 0.1, 0.2]],
            [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6]],
            [[0.2, 0.2, 0.6], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1]],
            [[0.1, 0.6, 0.3], [0.2, 0.3, 0.5], [0.2, 0.1, 0.7]],
            [[0.2, 0.6, 0.2], [0.1, 0.1, 0.8], [0.1, 0.4, 0.5]],
            [[0.5, 0.2, 0.3], [0.2, 0.1, 0.7], [0.4, 0.4, 0.2]],
            [[0.1, 0.5, 0.4], [0.4, 0.5, 0.1], [0.1, 0.3, 0.6]],
            [[0.5, 0.3, 0.2], [0.4, 0.2, 0.4], [0.7, 0.2, 0.1]],
            [[0.1, 0.1, 0.8], [0.2, 0.7, 0.1], [0.3, 0.4, 0.3]],
            [[0.4, 0.2, 0.4], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
            [[0.4, 0.2, 0.4], [0.3, 0.3, 0.4], [0.1, 0.5, 0.4]],
            [[0.2, 0.6, 0.2], [0.2, 0.4, 0.4], [0.3, 0.5, 0.2]],
            [[0.3, 0.1, 0.6], [0.3, 0.2, 0.5], [0.1, 0.4, 0.5]],
            [[0.2, 0.3, 0.5], [0.3, 0.2, 0.5], [0.1, 0.6, 0.3]],
            [[0.2, 0.5, 0.3], [0.2, 0.1, 0.7], [0.7, 0.1, 0.2]],
            [[0.6, 0.1, 0.3], [0.6, 0.2, 0.2], [0.5, 0.4, 0.1]],
            [[0.3, 0.4, 0.3], [0.6, 0.1, 0.3], [0.1, 0.7, 0.2]],
            [[0.3, 0.5, 0.2], [0.6, 0.2, 0.2], [0.2, 0.3, 0.5]],
            [[0.2, 0.2, 0.6], [0.4, 0.3, 0.3], [0.2, 0.4, 0.4]],
            [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.5, 0.4, 0.1]],
            [[0.2, 0.5, 0.3], [0.7, 0.2, 0.1], [0.3, 0.1, 0.6]],
            [[0.1, 0.8, 0.1], [0.1, 0.1, 0.8], [0.3, 0.1, 0.6]],
            [[0.1, 0.6, 0.3], [0.2, 0.6, 0.2], [0.2, 0.2, 0.6]],
            [[0.4, 0.5, 0.1], [0.7, 0.2, 0.1], [0.4, 0.3, 0.3]],
            [[0.3, 0.5, 0.2], [0.2, 0.6, 0.2], [0.3, 0.4, 0.3]],
            [[0.4, 0.1, 0.5], [0.2, 0.2, 0.6], [0.5, 0.4, 0.1]],
            [[0.2, 0.3, 0.5], [0.3, 0.5, 0.2], [0.3, 0.1, 0.6]],
            [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.5, 0.1, 0.4]],
            [[0.1, 0.8, 0.1], [0.4, 0.1, 0.5], [0.1, 0.4, 0.5]],
            [[0.2, 0.4, 0.4], [0.4, 0.2, 0.4], [0.5, 0.2, 0.3]],
            [[0.5, 0.4, 0.1], [0.4, 0.1, 0.5], [0.3, 0.4, 0.3]],
            [[0.4, 0.2, 0.4], [0.3, 0.4, 0.3], [0.3, 0.6, 0.1]],
            [[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.6, 0.2]],
            [[0.1, 0.5, 0.4], [0.4, 0.1, 0.5], [0.1, 0.4, 0.5]],
            [[0.5, 0.2, 0.3], [0.2, 0.7, 0.1], [0.3, 0.2, 0.5]],
            [[0.8, 0.1, 0.1], [0.2, 0.5, 0.3], [0.1, 0.2, 0.7]],
            [[0.2, 0.7, 0.1], [0.1, 0.4, 0.5], [0.7, 0.1, 0.2]],
            [[0.7, 0.1, 0.2], [0.2, 0.6, 0.2], [0.3, 0.3, 0.4]],
            [[0.5, 0.2, 0.3], [0.4, 0.4, 0.2], [0.6, 0.3, 0.1]],
            [[0.4, 0.5, 0.1], [0.8, 0.1, 0.1], [0.4, 0.1, 0.5]],
            [[0.2, 0.3, 0.5], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]],
            [[0.2, 0.2, 0.6], [0.6, 0.3, 0.1], [0.1, 0.2, 0.7]],
            [[0.3, 0.5, 0.2], [0.1, 0.7, 0.2], [0.4, 0.2, 0.4]],
            [[0.2, 0.4, 0.4], [0.6, 0.2, 0.2], [0.4, 0.3, 0.3]],
            [[0.2, 0.1, 0.7], [0.2, 0.3, 0.5], [0.3, 0.2, 0.5]],
            [[0.3, 0.1, 0.6], [0.2, 0.3, 0.5], [0.5, 0.3, 0.2]],
            [[0.3, 0.3, 0.4], [0.3, 0.4, 0.3], [0.5, 0.2, 0.3]],
            [[0.5, 0.3, 0.2], [0.1, 0.3, 0.6], [0.3, 0.1, 0.6]],
            [[0.4, 0.3, 0.3], [0.6, 0.3, 0.1], [0.6, 0.1, 0.3]],
            [[0.8, 0.1, 0.1], [0.1, 0.1, 0.8], [0.3, 0.2, 0.5]],
            [[0.2, 0.5, 0.3], [0.1, 0.6, 0.3], [0.3, 0.3, 0.4]],
            [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.1, 0.5, 0.4]],
            [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.4, 0.4, 0.2]],
            [[0.5, 0.4, 0.1], [0.5, 0.1, 0.4], [0.7, 0.1, 0.2]],
            [[0.5, 0.4, 0.1], [0.4, 0.2, 0.4], [0.4, 0.3, 0.3]],
            [[0.1, 0.6, 0.3], [0.4, 0.1, 0.5], [0.4, 0.2, 0.4]],
            [[0.1, 0.7, 0.2], [0.3, 0.6, 0.1], [0.1, 0.5, 0.4]],
            [[0.2, 0.5, 0.3], [0.7, 0.2, 0.1], [0.6, 0.1, 0.3]],
            [[0.3, 0.3, 0.4], [0.4, 0.2, 0.4], [0.1, 0.7, 0.2]],
            [[0.7, 0.1, 0.2], [0.3, 0.4, 0.3], [0.3, 0.3, 0.4]],
            [[0.2, 0.4, 0.4], [0.1, 0.2, 0.7], [0.1, 0.7, 0.2]],
            [[0.3, 0.6, 0.1], [0.2, 0.7, 0.1], [0.2, 0.2, 0.6]],
            [[0.4, 0.1, 0.5], [0.8, 0.1, 0.1], [0.6, 0.1, 0.3]],
            [[0.6, 0.2, 0.2], [0.4, 0.4, 0.2], [0.3, 0.3, 0.4]],
            [[0.1, 0.3, 0.6], [0.1, 0.2, 0.7], [0.6, 0.1, 0.3]],
            [[0.1, 0.5, 0.4], [0.2, 0.3, 0.5], [0.1, 0.6, 0.3]],
            [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.4, 0.5, 0.1]],
            [[0.5, 0.3, 0.2], [0.1, 0.1, 0.8], [0.4, 0.3, 0.3]],
            [[0.2, 0.1, 0.7], [0.4, 0.4, 0.2], [0.6, 0.1, 0.3]],
            [[0.5, 0.1, 0.4], [0.6, 0.1, 0.3], [0.4, 0.4, 0.2]],
            [[0.6, 0.1, 0.3], [0.2, 0.7, 0.1], [0.2, 0.3, 0.5]],
            [[0.8, 0.1, 0.1], [0.2, 0.6, 0.2], [0.4, 0.1, 0.5]],
            [[0.3, 0.6, 0.1], [0.2, 0.5, 0.3], [0.1, 0.7, 0.2]],
            [[0.3, 0.6, 0.1], [0.5, 0.4, 0.1], [0.5, 0.3, 0.2]],
            [[0.3, 0.1, 0.6], [0.1, 0.5, 0.4], [0.3, 0.3, 0.4]],
            [[0.4, 0.4, 0.2], [0.1, 0.1, 0.8], [0.2, 0.6, 0.2]],
            [[0.4, 0.2, 0.4], [0.3, 0.3, 0.4], [0.3, 0.6, 0.1]],
            [[0.3, 0.3, 0.4], [0.2, 0.2, 0.6], [0.1, 0.2, 0.7]],
            [[0.7, 0.2, 0.1], [0.1, 0.3, 0.6], [0.4, 0.2, 0.4]],
            [[0.2, 0.6, 0.2], [0.1, 0.5, 0.4], [0.3, 0.5, 0.2]],
            [[0.2, 0.3, 0.5], [0.1, 0.1, 0.8], [0.1, 0.7, 0.2]],
            [[0.4, 0.2, 0.4], [0.3, 0.1, 0.6], [0.1, 0.6, 0.3]],
            [[0.1, 0.6, 0.3], [0.3, 0.5, 0.2], [0.1, 0.7, 0.2]],
            [[0.2, 0.5, 0.3], [0.2, 0.3, 0.5], [0.2, 0.6, 0.2]],
            [[0.1, 0.1, 0.8], [0.1, 0.7, 0.2], [0.6, 0.3, 0.1]],
            [[0.3, 0.5, 0.2], [0.1, 0.1, 0.8], [0.4, 0.2, 0.4]],
            [[0.1, 0.2, 0.7], [0.1, 0.4, 0.5], [0.3, 0.5, 0.2]],
            [[0.7, 0.2, 0.1], [0.4, 0.1, 0.5], [0.5, 0.1, 0.4]],
            [[0.3, 0.4, 0.3], [0.1, 0.1, 0.8], [0.3, 0.1, 0.6]],
            [[0.6, 0.3, 0.1], [0.5, 0.4, 0.1], [0.5, 0.1, 0.4]],
            [[0.4, 0.5, 0.1], [0.3, 0.1, 0.6], [0.2, 0.1, 0.7]],
            [[0.1, 0.1, 0.8], [0.4, 0.2, 0.4], [0.3, 0.1, 0.6]],
            [[0.2, 0.7, 0.1], [0.5, 0.1, 0.4], [0.3, 0.2, 0.5]],
            [[0.2, 0.3, 0.5], [0.1, 0.5, 0.4], [0.5, 0.3, 0.2]],
            [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.4, 0.5, 0.1]],
            [[0.2, 0.1, 0.7], [0.4, 0.2, 0.4], [0.7, 0.2, 0.1]],
            [[0.2, 0.5, 0.3], [0.6, 0.3, 0.1], [0.2, 0.6, 0.2]],
            [[0.1, 0.1, 0.8], [0.7, 0.2, 0.1], [0.5, 0.3, 0.2]],
            [[0.4, 0.1, 0.5], [0.1, 0.5, 0.4], [0.1, 0.3, 0.6]],
            [[0.4, 0.2, 0.4], [0.2, 0.4, 0.4], [0.5, 0.3, 0.2]],
            [[0.4, 0.3, 0.3], [0.6, 0.1, 0.3], [0.7, 0.2, 0.1]],
            [[0.1, 0.8, 0.1], [0.5, 0.4, 0.1], [0.4, 0.5, 0.1]],
            [[0.2, 0.4, 0.4], [0.3, 0.1, 0.6], [0.6, 0.1, 0.3]],
            [[0.8, 0.1, 0.1], [0.2, 0.4, 0.4], [0.2, 0.2, 0.6]],
            [[0.6, 0.1, 0.3], [0.2, 0.4, 0.4], [0.2, 0.3, 0.5]],
            [[0.2, 0.2, 0.6], [0.4, 0.5, 0.1], [0.1, 0.5, 0.4]],
            [[0.2, 0.5, 0.3], [0.3, 0.5, 0.2], [0.6, 0.2, 0.2]],
            [[0.1, 0.5, 0.4], [0.7, 0.2, 0.1], [0.2, 0.2, 0.6]],
            [[0.2, 0.3, 0.5], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2]],
            [[0.3, 0.2, 0.5], [0.3, 0.6, 0.1], [0.4, 0.4, 0.2]],
            [[0.4, 0.3, 0.3], [0.4, 0.2, 0.4], [0.6, 0.2, 0.2]],
            [[0.1, 0.3, 0.6], [0.3, 0.2, 0.5], [0.1, 0.1, 0.8]],
            [[0.3, 0.5, 0.2], [0.5, 0.1, 0.4], [0.2, 0.5, 0.3]],
            [[0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.1, 0.5, 0.4]],
            [[0.2, 0.6, 0.2], [0.1, 0.1, 0.8], [0.4, 0.2, 0.4]],
            [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.6, 0.1, 0.3]],
            [[0.5, 0.1, 0.4], [0.1, 0.7, 0.2], [0.3, 0.2, 0.5]],
            [[0.1, 0.6, 0.3], [0.4, 0.2, 0.4], [0.2, 0.1, 0.7]],
            [[0.1, 0.5, 0.4], [0.5, 0.1, 0.4], [0.3, 0.5, 0.2]],
            [[0.6, 0.3, 0.1], [0.1, 0.8, 0.1], [0.2, 0.3, 0.5]],
            [[0.5, 0.3, 0.2], [0.2, 0.4, 0.4], [0.3, 0.2, 0.5]],
            [[0.2, 0.4, 0.4], [0.1, 0.6, 0.3], [0.8, 0.1, 0.1]],
            [[0.3, 0.3, 0.4], [0.2, 0.3, 0.5], [0.4, 0.3, 0.3]],
            [[0.3, 0.3, 0.4], [0.6, 0.3, 0.1], [0.2, 0.6, 0.2]],
            [[0.1, 0.7, 0.2], [0.1, 0.4, 0.5], [0.5, 0.3, 0.2]],
            [[0.4, 0.1, 0.5], [0.5, 0.4, 0.1], [0.5, 0.2, 0.3]],
            [[0.3, 0.1, 0.6], [0.5, 0.1, 0.4], [0.1, 0.3, 0.6]],
            [[0.6, 0.2, 0.2], [0.3, 0.4, 0.3], [0.2, 0.3, 0.5]],
            [[0.1, 0.5, 0.4], [0.3, 0.3, 0.4], [0.2, 0.4, 0.4]],
            [[0.5, 0.4, 0.1], [0.3, 0.6, 0.1], [0.6, 0.3, 0.1]],
            [[0.4, 0.1, 0.5], [0.7, 0.2, 0.1], [0.5, 0.2, 0.3]],
            [[0.3, 0.4, 0.3], [0.1, 0.3, 0.6], [0.1, 0.8, 0.1]],
            [[0.8, 0.1, 0.1], [0.5, 0.2, 0.3], [0.4, 0.5, 0.1]],
            [[0.3, 0.1, 0.6], [0.3, 0.4, 0.3], [0.2, 0.2, 0.6]],
            [[0.7, 0.1, 0.2], [0.6, 0.2, 0.2], [0.3, 0.5, 0.2]],
            [[0.5, 0.2, 0.3], [0.7, 0.2, 0.1], [0.4, 0.4, 0.2]],
            [[0.7, 0.1, 0.2], [0.4, 0.5, 0.1], [0.2, 0.6, 0.2]],
            [[0.5, 0.4, 0.1], [0.2, 0.1, 0.7], [0.8, 0.1, 0.1]],
            [[0.2, 0.1, 0.7], [0.6, 0.3, 0.1], [0.1, 0.4, 0.5]],
            [[0.5, 0.1, 0.4], [0.4, 0.4, 0.2], [0.4, 0.3, 0.3]],
            [[0.6, 0.2, 0.2], [0.8, 0.1, 0.1], [0.3, 0.4, 0.3]],
            [[0.4, 0.3, 0.3], [0.3, 0.6, 0.1], [0.5, 0.1, 0.4]],
            [[0.7, 0.1, 0.2], [0.2, 0.4, 0.4], [0.5, 0.1, 0.4]],
            [[0.2, 0.7, 0.1], [0.2, 0.4, 0.4], [0.5, 0.4, 0.1]],
            [[0.1, 0.8, 0.1], [0.6, 0.1, 0.3], [0.5, 0.4, 0.1]],
            [[0.3, 0.4, 0.3], [0.1, 0.2, 0.7], [0.4, 0.5, 0.1]],
            [[0.1, 0.1, 0.8], [0.5, 0.3, 0.2], [0.2, 0.1, 0.7]],
            [[0.4, 0.2, 0.4], [0.1, 0.6, 0.3], [0.2, 0.3, 0.5]],
            [[0.7, 0.1, 0.2], [0.1, 0.7, 0.2], [0.2, 0.6, 0.2]],
            [[0.5, 0.3, 0.2], [0.6, 0.1, 0.3], [0.4, 0.4, 0.2]],
            [[0.2, 0.3, 0.5], [0.2, 0.6, 0.2], [0.6, 0.2, 0.2]],
            [[0.5, 0.2, 0.3], [0.5, 0.3, 0.2], [0.3, 0.1, 0.6]],
            [[0.1, 0.2, 0.7], [0.1, 0.7, 0.2], [0.7, 0.2, 0.1]],
            [[0.1, 0.3, 0.6], [0.3, 0.5, 0.2], [0.2, 0.7, 0.1]],
            [[0.1, 0.8, 0.1], [0.2, 0.1, 0.7], [0.4, 0.1, 0.5]],
            [[0.1, 0.8, 0.1], [0.1, 0.7, 0.2], [0.1, 0.5, 0.4]],
            [[0.2, 0.4, 0.4], [0.1, 0.6, 0.3], [0.5, 0.3, 0.2]],
            [[0.1, 0.7, 0.2], [0.1, 0.8, 0.1], [0.3, 0.4, 0.3]],
            [[0.5, 0.1, 0.4], [0.3, 0.1, 0.6], [0.2, 0.3, 0.5]],
            [[0.1, 0.4, 0.5], [0.5, 0.1, 0.4], [0.1, 0.6, 0.3]],
            [[0.5, 0.1, 0.4], [0.2, 0.4, 0.4], [0.4, 0.3, 0.3]],
            [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.1, 0.1, 0.8]],
            [[0.1, 0.7, 0.2], [0.1, 0.8, 0.1], [0.3, 0.1, 0.6]],
            [[0.1, 0.7, 0.2], [0.6, 0.3, 0.1], [0.2, 0.3, 0.5]],
            [[0.3, 0.2, 0.5], [0.1, 0.1, 0.8], [0.4, 0.4, 0.2]],
            [[0.3, 0.6, 0.1], [0.7, 0.2, 0.1], [0.6, 0.3, 0.1]],
            [[0.3, 0.3, 0.4], [0.5, 0.2, 0.3], [0.4, 0.2, 0.4]],
            [[0.1, 0.6, 0.3], [0.3, 0.1, 0.6], [0.5, 0.1, 0.4]],
            [[0.5, 0.3, 0.2], [0.8, 0.1, 0.1], [0.1, 0.5, 0.4]],
            [[0.1, 0.5, 0.4], [0.5, 0.3, 0.2], [0.2, 0.6, 0.2]],
            [[0.2, 0.4, 0.4], [0.5, 0.3, 0.2], [0.4, 0.1, 0.5]],
            [[0.2, 0.3, 0.5], [0.1, 0.5, 0.4], [0.3, 0.5, 0.2]],
            [[0.4, 0.3, 0.3], [0.7, 0.1, 0.2], [0.1, 0.8, 0.1]],
            [[0.7, 0.2, 0.1], [0.4, 0.5, 0.1], [0.6, 0.1, 0.3]],
            [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.1, 0.4, 0.5]],
            [[0.1, 0.2, 0.7], [0.2, 0.4, 0.4], [0.1, 0.3, 0.6]],
            [[0.1, 0.8, 0.1], [0.1, 0.3, 0.6], [0.6, 0.3, 0.1]],
            [[0.8, 0.1, 0.1], [0.4, 0.2, 0.4], [0.4, 0.5, 0.1]],
            [[0.5, 0.2, 0.3], [0.1, 0.4, 0.5], [0.1, 0.1, 0.8]],
            [[0.1, 0.8, 0.1], [0.1, 0.3, 0.6], [0.5, 0.1, 0.4]],
            [[0.5, 0.2, 0.3], [0.4, 0.3, 0.3], [0.3, 0.2, 0.5]],
            [[0.4, 0.3, 0.3], [0.7, 0.1, 0.2], [0.1, 0.7, 0.2]],
            [[0.2, 0.3, 0.5], [0.2, 0.7, 0.1], [0.2, 0.2, 0.6]],
            [[0.2, 0.6, 0.2], [0.3, 0.6, 0.1], [0.4, 0.3, 0.3]],
            [[0.2, 0.6, 0.2], [0.1, 0.2, 0.7], [0.5, 0.1, 0.4]],
            [[0.4, 0.4, 0.2], [0.1, 0.2, 0.7], [0.3, 0.1, 0.6]],
            [[0.5, 0.3, 0.2], [0.2, 0.2, 0.6], [0.4, 0.4, 0.2]],
            [[0.5, 0.1, 0.4], [0.5, 0.4, 0.1], [0.6, 0.2, 0.2]],
            [[0.3, 0.1, 0.6], [0.1, 0.3, 0.6], [0.4, 0.1, 0.5]],
            [[0.1, 0.8, 0.1], [0.4, 0.4, 0.2], [0.3, 0.2, 0.5]],
            [[0.3, 0.2, 0.5], [0.5, 0.1, 0.4], [0.1, 0.3, 0.6]],
            [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.4, 0.4, 0.2]],
            [[0.7, 0.2, 0.1], [0.1, 0.3, 0.6], [0.4, 0.2, 0.4]],
            [[0.1, 0.8, 0.1], [0.6, 0.3, 0.1], [0.4, 0.5, 0.1]],
            [[0.3, 0.1, 0.6], [0.4, 0.1, 0.5], [0.5, 0.3, 0.2]],
            [[0.5, 0.1, 0.4], [0.3, 0.2, 0.5], [0.4, 0.4, 0.2]],
            [[0.1, 0.3, 0.6], [0.6, 0.2, 0.2], [0.8, 0.1, 0.1]],
            [[0.1, 0.3, 0.6], [0.6, 0.3, 0.1], [0.5, 0.3, 0.2]],
            [[0.1, 0.7, 0.2], [0.1, 0.1, 0.8], [0.2, 0.4, 0.4]],
            [[0.5, 0.1, 0.4], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1]],
            [[0.2, 0.2, 0.6], [0.1, 0.7, 0.2], [0.4, 0.4, 0.2]],
            [[0.5, 0.2, 0.3], [0.2, 0.1, 0.7], [0.2, 0.4, 0.4]],
            [[0.1, 0.3, 0.6], [0.3, 0.1, 0.6], [0.2, 0.2, 0.6]],
            [[0.1, 0.3, 0.6], [0.1, 0.8, 0.1], [0.6, 0.2, 0.2]],
            [[0.2, 0.3, 0.5], [0.3, 0.6, 0.1], [0.1, 0.6, 0.3]],
            [[0.2, 0.5, 0.3], [0.2, 0.4, 0.4], [0.6, 0.1, 0.3]],
            [[0.2, 0.6, 0.2], [0.6, 0.3, 0.1], [0.1, 0.5, 0.4]],
            [[0.5, 0.2, 0.3], [0.6, 0.2, 0.2], [0.4, 0.3, 0.3]],
            [[0.4, 0.3, 0.3], [0.1, 0.3, 0.6], [0.4, 0.1, 0.5]],
            [[0.2, 0.4, 0.4], [0.8, 0.1, 0.1], [0.1, 0.7, 0.2]],
            [[0.1, 0.5, 0.4], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1]],
            [[0.2, 0.2, 0.6], [0.3, 0.4, 0.3], [0.2, 0.3, 0.5]],
            [[0.5, 0.2, 0.3], [0.3, 0.3, 0.4], [0.1, 0.6, 0.3]],
            [[0.1, 0.8, 0.1], [0.4, 0.2, 0.4], [0.1, 0.6, 0.3]],
            [[0.4, 0.3, 0.3], [0.8, 0.1, 0.1], [0.6, 0.2, 0.2]],
            [[0.6, 0.3, 0.1], [0.2, 0.6, 0.2], [0.2, 0.3, 0.5]],
            [[0.4, 0.5, 0.1], [0.7, 0.1, 0.2], [0.2, 0.6, 0.2]],
            [[0.2, 0.4, 0.4], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]],
            [[0.1, 0.4, 0.5], [0.5, 0.4, 0.1], [0.4, 0.3, 0.3]],
            [[0.3, 0.4, 0.3], [0.2, 0.7, 0.1], [0.5, 0.2, 0.3]],
            [[0.1, 0.2, 0.7], [0.4, 0.4, 0.2], [0.3, 0.6, 0.1]],
            [[0.1, 0.7, 0.2], [0.1, 0.5, 0.4], [0.1, 0.4, 0.5]],
            [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.5, 0.2]],
            [[0.3, 0.5, 0.2], [0.1, 0.3, 0.6], [0.2, 0.5, 0.3]],
            [[0.7, 0.1, 0.2], [0.1, 0.5, 0.4], [0.6, 0.3, 0.1]],
            [[0.1, 0.4, 0.5], [0.2, 0.5, 0.3], [0.7, 0.1, 0.2]],
            [[0.7, 0.1, 0.2], [0.2, 0.2, 0.6], [0.2, 0.1, 0.7]],
            [[0.2, 0.6, 0.2], [0.2, 0.3, 0.5], [0.3, 0.3, 0.4]],
            [[0.4, 0.3, 0.3], [0.3, 0.2, 0.5], [0.6, 0.2, 0.2]],
            [[0.4, 0.2, 0.4], [0.2, 0.1, 0.7], [0.3, 0.3, 0.4]],
            [[0.3, 0.4, 0.3], [0.7, 0.1, 0.2], [0.4, 0.2, 0.4]],
            [[0.7, 0.2, 0.1], [0.7, 0.1, 0.2], [0.2, 0.4, 0.4]],
            [[0.2, 0.4, 0.4], [0.4, 0.1, 0.5], [0.3, 0.2, 0.5]],
            [[0.2, 0.1, 0.7], [0.1, 0.5, 0.4], [0.3, 0.2, 0.5]],
            [[0.3, 0.4, 0.3], [0.5, 0.1, 0.4], [0.4, 0.3, 0.3]],
            [[0.1, 0.5, 0.4], [0.6, 0.3, 0.1], [0.4, 0.3, 0.3]],
            [[0.1, 0.6, 0.3], [0.1, 0.2, 0.7], [0.8, 0.1, 0.1]],
            [[0.1, 0.2, 0.7], [0.2, 0.4, 0.4], [0.2, 0.7, 0.1]],
            [[0.1, 0.4, 0.5], [0.6, 0.1, 0.3], [0.1, 0.3, 0.6]],
            [[0.3, 0.6, 0.1], [0.1, 0.5, 0.4], [0.1, 0.1, 0.8]],
            [[0.1, 0.1, 0.8], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3]],
            [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6], [0.3, 0.2, 0.5]],
            [[0.7, 0.1, 0.2], [0.4, 0.5, 0.1], [0.6, 0.2, 0.2]],
            [[0.1, 0.2, 0.7], [0.1, 0.8, 0.1], [0.1, 0.7, 0.2]],
            [[0.1, 0.4, 0.5], [0.1, 0.5, 0.4], [0.2, 0.2, 0.6]],
            [[0.1, 0.1, 0.8], [0.1, 0.8, 0.1], [0.8, 0.1, 0.1]],
            [[0.1, 0.2, 0.7], [0.2, 0.7, 0.1], [0.7, 0.1, 0.2]],
            [[0.1, 0.3, 0.6], [0.3, 0.6, 0.1], [0.6, 0.1, 0.3]],
            [[0.2, 0.1, 0.7], [0.7, 0.2, 0.1], [0.6, 0.1, 0.3]]]


class DQN:
    def __init__(self, input_shape: tuple):
        self.action_area: List[List[float]] = action_area()
        self.hidden_units = 64
        self.input_dim: int = input_shape[0] * input_shape[1]
        self.action_size: int = len(self.action_area)
        self.gamma: float = 0.95  # 折扣率
        self.epsilon: float = 1.0  # 随机探索率
        self.epsilon_min: float = 0.05  # 最低随机探索率
        self.epsilon_decay: float = 0.996  # 探索率下降指数
        self.learning_rate: float = 0.0005  # 学习率
        self.batch_size: int = 32
        self.memory: ReplyMemory = ReplyMemory()
        self.target_model = self._build_model()  # 目标模型
        self.policy_model = self._build_model()  # 策略模型
        self.dataset = None

    def _build_model(self):
        # with tf.device('/gpu:0'):
        # 用于深度q学习模型的神经网络
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(128, input_dim=self.input_dim, activation='relu'))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, _state, _action, reward, _next_state):
        #  储存回放缓存
        self.memory.push(_state, _action, reward, _next_state)

    def act(self, state, is_best=False):
        #  进行探索
        #  随机探索
        if np.random.rand() <= self.epsilon and not is_best:
            action = random.choice(self.action_area)
            action_index = self.action_area.index(action)
            return action, action_index  # 返回随机路径
        value = np.array(self.target_model(state))
        max_index = np.argmax(value)
        return self.action_area[max_index], max_index

    def build_dataset(self):
        #  取小批量数据优化模型
        minibatch: list = self.memory.sample(self.batch_size * 5)
        data = []
        labels = []
        # with tf.device('/gpu:0'):
        for _state, _action, reward, _next_state in minibatch:
            """当前状态和下一个状态下策略网络的预测值"""
            policy_value = np.array(self.policy_model(_state))  # 当前状态下的所有预测值
            policy_next_value = self.policy_model(_next_state)  # 下个状态下的所有预测值
            """下一个状态目标网络的所有预测值，并计算下一个状态下所有action带来的奖励中最高的"""
            target_value = self.target_model(_next_state)
            policy_action = np.argmax(policy_next_value[0])
            policy_value[0][_action] = reward + self.gamma * target_value[0][policy_action]
            """更新策略网络，每一个minibatch结束后将权重复制到minibatch中"""
            # self.policy_model.fit(_state, policy_value, epochs=1, verbose=0)
            data.append(_state)
            labels.append(policy_value)
        # 创建数据集对象
        self.dataset = tf.data.Dataset.from_tensor_slices((data, labels))

    def replay(self):
        self.policy_model.fit(self.dataset, batch_size=self.batch_size, epochs=_epochs, use_multiprocessing=True,
                              verbose=0)
        #  降低随机探索的概率
        if self.epsilon > self.epsilon_min:

            self.epsilon *= self.epsilon_decay
        # 复制模型的权重
        self.target_model.set_weights(self.policy_model.get_weights())
