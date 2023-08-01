# 测试文件是否存在
import os
import time

# 你想测试一个文件或目录是否存在。
print(os.path.exists('D:/python_work/Leetcode/CookBook/IO/1.txt'))
print(os.path.exists('/tmp/spam'))

# 是常规文件
os.path.isfile('D:/python_work/Leetcode/CookBook/IO/1.txt')

# 是一个目录
os.path.isdir('D:/python_work/Leetcode/CookBook/IO')

# 是一个符号链接
print(os.path.islink('/usr/local/bin/python3'))

# 获取链接到的文件
print(os.path.realpath('/usr/local/bin/python3'))


print(os.path.getsize('D:/python_work/Leetcode/CookBook/IO/1.txt'))
print(os.path.getmtime('D:/python_work/Leetcode/CookBook/IO/1.txt'))
print(time.ctime(os.path.getmtime('D:/python_work/Leetcode/CookBook/IO/1.txt')))




