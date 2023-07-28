# 同时迭代多个序列
from itertools import zip_longest

# 你想同时迭代多个序列，每次分别从一个序列中取一个元素。
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# 迭代长度和最短序列一致
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

for i in zip_longest(a, b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)


# 生成字典
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)


# 接受多余两个的序列参数
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)




