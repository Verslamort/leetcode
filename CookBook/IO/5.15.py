# 打印不合法的文件名
import os


# 你的程序获取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程序崩溃，出现了
# UnicodeEncodeError 异常和一条奇怪的消息—— surrogates not allowed 。
def bad_filename(filename):
    return repr(filename)[1:-1]


try:
    print('ABC.txt')
except UnicodeEncodeError:
    print(bad_filename('ABC.txt'))


files = os.listdir('.')
print(files)


