# 解压序列赋值给多个变量

p = (4, 5)
x, y = p
print(x)
print(y)

s = 'hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
