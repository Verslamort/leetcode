# 查找两字典的相同点

# 怎样在两个字典中寻寻找相同点(比如相同的键、相同的值等等)？
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 在两字典的keys()或者items()方法返回结果上执行集合操作
print(type(a.keys()))
print(a.keys() & b.keys())
print(a.keys() - b.keys())

print(a.items())
print(a.items() & b.items())

# 也可以用于修改或者过滤字典元素
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

