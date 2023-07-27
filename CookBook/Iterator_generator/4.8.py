# 跳过可迭代对象的开始部分
from itertools import dropwhile, islice

# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
with open('./1.txt') as f:
    for line in f:
        print(line, end='')
print('-----')
# 跳过注释
with open('./1.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


# 明确知道要跳过的元素个数
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)



