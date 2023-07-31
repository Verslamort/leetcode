# 固定大小记录的文件迭代
from functools import partial


# 你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代。
RECORD_SIZE = 32
with open('example.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)


