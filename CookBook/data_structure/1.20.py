# 合并多个字典或映射
from collections import ChainMap

# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在。
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(a)


values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13
print(merged['x'])

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x']) # Notice change to merged dicts)


