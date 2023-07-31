# 读写压缩文件
import gzip
import bz2


# 你想读写一个gzip或bz2格式的压缩文件。
# gzip
with gzip.open('1.tar.gz', 'rb') as f:
    text = f.read()
    print(text)

# bz2
with bz2.open('3.bz2', 'rb') as f:
    text = f.read()
    print(text)


