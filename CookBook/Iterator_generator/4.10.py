# 序列上索引值迭代
from collections import defaultdict


# 你想在迭代一个序列的同时跟踪正在被处理的元素索引。
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):  # 可传递开始参数
    print(idx, val)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


word_summary = defaultdict(list)
with open('./1.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

