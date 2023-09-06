def reword_for_hash_rate(delay) -> float:
    """分段函数，前半段为二次函数，后半段为反比例函数"""
    """如果当前时间片没有处理通信任务就返回一个比较小的奖励值"""
    if delay == -1:
        return 0.07
    elif delay <= 0:
        return 1
    elif delay <= 0.1:
        return 80 * (delay ** 2) - 16 * delay + 1
    elif delay > 0.1:
        return 1 / (50 * delay)


if __name__ == '__main__':
    for i in range(100):
        print(f"时延为:{i / 100},奖励值为:{reword_for_hash_rate(i / 100)}")
