#  顺序迭代合并后的排序迭代对象
import heapq


# 你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)


with open('./sorted_file_1.py', 'rt') as file1, \
    open('./sorted_file_2.py', 'rt') as file2, \
    open('./merged_file.py', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)


