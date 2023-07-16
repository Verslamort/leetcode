import queue


def demo1():
    # list 当队列
    q1 = []
    for i in range(10):
        q1.append(i)
    print(len(q1))
    while q1:
        item = q1.pop(0)
        print(item)
    print(q1)

def really_queue():
    q2 = queue.Queue()
    for i in range(10):
        q2.put(i)
    print(q2.empty())
    while not q2.empty():
        item = q2.get()
        print(item)
    print(q2.empty())


if __name__ == '__main__':
    demo1()
    really_queue()