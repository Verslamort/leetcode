# 转换并同时计算数据
import os


# 你需要在数据序列上执行聚集函数(比如 sum() , min() , max() )，但是首先你需要先转换或者过滤数据
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

files = os.listdir('..')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])  # 省内存

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_share = min(portfolio, key=lambda s: s['shares'])
print(min_share)
