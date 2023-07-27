# 排列组合的迭代
from itertools import permutations, combinations, combinations_with_replacement

# 你想迭代遍历一个集合中元素的所有可能的排列或组合
items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
print('-----')

# 制定长度
for p in permutations(items, 2):
    print(p)
print('-----')

# 元素不同，无序
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)
for c in combinations(items, 1):
    print(c)


# 同一个元素可被选中多次
for c in combinations_with_replacement(items, 3):
    print(c)





