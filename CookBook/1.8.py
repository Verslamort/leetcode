# 字典的运算

# 怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 为了对字典值执行计算操作，通常需要使用zip()函数先将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))  # zip()函数创建的是一个只能访问一次的迭代器
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

# 使用zip()和sorted()函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)


# key函数参数来获取最小值或最大值对应的键的信息
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
# 最小值，还需执行一次查找操作
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)


# 当多个实体拥有相同的值的时候，键会决定返回结果
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))


