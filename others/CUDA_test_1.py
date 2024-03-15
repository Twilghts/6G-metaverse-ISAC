import tensorflow as tf
from tensorflow.python.client import device_lib as _device_lib, device_lib
import time
import timeit
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 代码用于忽略级别 2 及以下的消息（级别 1 是提示，级别 2 是警告，级别 3 是错误）。
time_1 = time.perf_counter()
with tf.device('/cpu:0'):
    time_2 = time.perf_counter()
    cpu_a = tf.random.normal([10000, 1000])
    cpu_b = tf.random.normal([1000, 2000])
    print(cpu_a.device, cpu_b.device)
    print(f"创建数组时间:{time.perf_counter() - time_2}")
print(f"启动设备+创建数组时间:{time.perf_counter() - time_1}")
time_1 = time.perf_counter()
with tf.device('/gpu:0'):
    time_2 = time.perf_counter()
    gpu_a = tf.random.normal([10000, 1000])
    gpu_b = tf.random.normal([1000, 2000])
    print(gpu_a.device, gpu_b.device)
    print(f"创建数组时间:{time.perf_counter() - time_2}")
print(f"启动设备+创建数组时间:{time.perf_counter() - time_1}")


def cpu_run():
    with tf.device('/cpu:0'):
        c = tf.matmul(cpu_a, cpu_b)
    return c


def gpu_run():
    with tf.device('/gpu:0'):
        c = tf.matmul(gpu_a, gpu_b)
    return c


# warm up
cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=100)
print('warmup:', cpu_time, gpu_time)

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=100)
print('run time:', cpu_time, gpu_time)

print('GPU', tf.test.is_gpu_available())
#
# gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
# print(gpus)
#
# local_device_protos = device_lib.list_local_devices()
# devices = [_t.name for _t in local_device_protos]
# for d in devices:
#     print(d)
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())
#
# # 定义一个使用 GPU 的操作
# with tf.device('/GPU:0'):
#     # 在此处添加 GPU 上的操作
#     pass
#
# # 定义一个使用 CPU 的操作
# with tf.device('/CPU:0'):
#     # 在此处添加 CPU 上的操作
#     pass
#
# 检查 GPU 是否可见
# gpus = tf.config.list_physical_devices('GPU')
# if gpus:
#     # 设置 GPU 内存增长选项（可选）
#     for gpu in gpus:
#         tf.config.experimental.set_memory_growth(gpu, True)
#
#     # 在可见的 GPU 上设置默认设备
#     tf.config.experimental.set_visible_devices(gpus, 'GPU')

# 在此处构建和训练模型
