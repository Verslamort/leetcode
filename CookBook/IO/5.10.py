# 内存映射的二进制文件
import os
import mmap


# 你想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它的内容或者是原地做些修改。
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')


m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

# 重新分配
m[0:11] = b'Hello World'
m.close()
# 验证
with open('data', 'rb') as f:
    print(f.read(11))

with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

print(m.closed)


m = memory_map('data')
# 无符号整数的内存视图
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])




