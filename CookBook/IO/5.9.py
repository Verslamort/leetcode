# 读取二进制数据到可变缓冲区中
import os


# 你想直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。或者你想原地修改数据并将它写回到一个文件中去。
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)
with open('newsample.bin', 'wb') as f:
    f.write(buf)



print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)





