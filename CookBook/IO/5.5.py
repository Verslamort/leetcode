# 文件不存在才能写入
import os


# 你想向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。也就是不允许覆盖已存在的文件内容。
with open('file.txt', 'xt') as f:
    f.write('Hello\n')


if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')


