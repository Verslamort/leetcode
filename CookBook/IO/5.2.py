# 打印输出至文件中

# 你想将print()函数的输出重定向到一个文件中去。
with open('./3.txt', 'wt') as f:
    print('Hello World!', file=f)

