# 从字典中提取子集

# 你想构造一个字典，它是另外一个字典的子集。
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# p1 = {key: value for key, value in prices.items() if value > 200}
p1 = dict((key, value) for key, value in prices.items() if value > 200)  # 元组
print(p1)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)



