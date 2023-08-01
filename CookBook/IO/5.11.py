# 文件路径名的操作
import os


# 你需要使用路径名来获取文件名，目录名，绝对路径等等。
path = 'D:/python_work/Leetcode/CookBook/IO/5.10.py'
# 获取路径的最后一个组件
print(os.path.basename(path))

# 获取目录名
print(os.path.dirname(path))

# 将路径组件连接在一起
print(os.path.join('tmp', 'data', os.path.basename(path)))

# 展开用户的主目录
path = '~/CookBook/IO/5.10.py'
print(os.path.expanduser(path))

# 拆分文件扩展名
print(os.path.splitext(path))



