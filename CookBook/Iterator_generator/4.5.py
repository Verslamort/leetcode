# 反向迭代

# 你想反方向迭代一个序列
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


f = open('./1.txt')
for line in reversed(list(f)):
    print(line, end='')
print('---')


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)
print('---')
for rr in Countdown(30):
    print(rr)




