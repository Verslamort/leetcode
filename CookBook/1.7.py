# 字典排序
from collections import OrderedDict


# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])


if __name__ == '__main__':
    ordered_dict()
