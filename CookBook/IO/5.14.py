# 忽略文件名编码
import os
import sys


# 你想使用原始文件名执行文件的I/O操作，也就是说文件名并没有经过系统默认编码去解码或编码过。
print(sys.getfilesystemencoding())

# 使用unicode文件名创建文件
with open('./xf1o.txt', 'w') as f:
    f.write('Spicy!')

# 目录列表（已解码）
print(os.listdir('.'))

# 目录列表（原始）
print(os.listdir(b'.'))

# 使用原始文件名打开文件
with open(b'xf1o.txt') as f:
    print(f.read())


