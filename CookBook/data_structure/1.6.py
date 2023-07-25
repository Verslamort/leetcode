# 字典中的键映射多个值
from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


d = defaultdict(list)  # defaultdict自动初始化每个key刚开始对应的值
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# setdefault必须创建一个新的初始值的实例
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)


# 多值映射字典
pairs = [[1, 2], [3, 4]]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

