# 读写字节数据
import array


# 你想读写二进制文件，比如图片，声音文件等等。
file = open('example.dat', 'wb')
file.write(b'100')
file.close()

with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)


# Text string
t = 'Hello World'
print(t[0])
for c in t:
    print(c)

# Byte string
b = b'Hello World'
print(b[0])
for c in b:
    print(c)


with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)


a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

print(a)






