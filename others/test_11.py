import random

from net_related.net import Net

if __name__ == '__main__':
    net = Net()
    router = random.choice(list(net.routers.values()))
    print(router)