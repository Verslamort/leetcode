# 创建数据处理管道
import bz2
import fnmatch
import gzip
import os
import re


# 你想以数据管道(类似Unix管道)的方式迭代处理数据。比如，你有个大量的数据需要处理，但是不能将它们一次性放入内存中。
def gen_find(filepath, top):
    """在目录树中查找与shell通配符模式匹配的所有文件名"""
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepath):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    打开一系列文件名，每次一个，生成一个文件对象。
    在进行下一次迭代时，文件将立即关闭。
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """将迭代器序列链接到一个序列中"""
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """在一系列行中查找正则表达式模式"""
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == '__main__':
    lognames = gen_find('./1.txt', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)

    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))






