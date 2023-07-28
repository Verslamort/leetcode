# 不同集合上元素的迭代
from itertools import chain


# 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环。
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)


active_items = set('runoob')
inactive_items = set('google')

for item in chain(active_items, inactive_items):
    print(item)


