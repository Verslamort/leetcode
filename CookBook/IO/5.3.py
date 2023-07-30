# 使用其他分隔符或行终止符打印

# 你想使用print()函数输出数据，但是想改变默认的分隔符或者行尾符。
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')


for i in range(5):
    print(i)


for i in range(5):
    print(i, end=' ')


print('\n', ','.join('ACME'))

row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row))
print(*row, sep=',')




