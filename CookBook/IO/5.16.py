# 增加或改变已打开文件的编码
import io
import sys
import urllib.request


# 你想在不关闭一个已打开的文件前提下增加或改变它的Unicode编码。
# u = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(u, encoding='utf-8')
# text = f.read()


# 修改一个已经打开的文本模式的文件的编码方式
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
# 可能中断终端


f = open('./1.txt', 'w')
print(f)  # io.TextIOWrapper 是一个编码和解码Unicode的文本处理层
print(f.buffer)  # 处理二进制数据的带缓冲的I/O层
print(f.buffer.raw)  # 表示操作系统底层文件描述符的原始文件


b = f.detach()
print(f)
print(b)
a = io.TextIOWrapper(b, encoding='latin-1')
print(a)


# 利用这种技术来改变文件行处理、错误机制以及文件处理的其他方面
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')



