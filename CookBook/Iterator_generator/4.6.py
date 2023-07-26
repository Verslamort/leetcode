# 带有外部状态的生成器函数
from collections import deque


# 你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('./1.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')


f = open('./1.txt')
lines = linehistory(f)
it = iter(lines)
print(next(it))
print(next(it))




