# 使用生成器创建新的迭代模式

# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
def frange(start, stop, increment):  # 生成器函数
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
    n -= 1
    print('Done!')


c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))



