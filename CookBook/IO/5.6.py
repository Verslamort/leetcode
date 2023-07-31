# 字符串的I/O操作
import io


# 你想使用操作类文件对象的程序来操作文本或二进制字符串。
s = io.StringIO()
print(s.write('Hello World\n'))
print('This is a test', file=s)
print(s.getvalue())

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())


# 操作二进制数据
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())




