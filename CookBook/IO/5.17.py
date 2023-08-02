# 将字节写入文本文件
import sys


# 你想在文本模式打开的文件中写入原始的字节数据。
sys.stdout.write('Hello\n')
sys.stdout.buffer.write(b'Hello\n')

