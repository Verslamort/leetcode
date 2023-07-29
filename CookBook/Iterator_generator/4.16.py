# 迭代器代替while无限循环
import sys


# 你在代码中使用while循环来迭代处理数据，因为它需要调用某个函数或者和一般迭代模式不同的测试条件。能不能用迭代器来重写这个循环呢？
CHUNKSIZE = 8192

f = open('./1.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)


