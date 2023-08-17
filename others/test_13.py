from collections import deque

set_1 = set()
for i in range(10):
    set_1.add(i)
for i in set_1:
    print(i)

print([n for n in range(2, 15, 3)])

test_deque = deque()
print(len(test_deque))
test_deque.append(1)
print(len(test_deque))
test_deque.append(2)
print(len(test_deque))
test_deque.append(3)
print(len(test_deque))

list_1 = []
print(f"结果是{sum(list_1) + len(list_1)}")