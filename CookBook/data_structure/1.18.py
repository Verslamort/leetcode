# 映射名称到序列元素

# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读，于是你想通过名称来访问元素。
# namedtuple
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 支持索引，解压
print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# 普通元组
def compute_cost(records):
    total = 0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# 命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute(records):
    global s
    total = 0
    for rec in records:
        s = Stock(*rec)
    total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
s = s._replace(shares=75)
print(s)


# 填充数据
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))




