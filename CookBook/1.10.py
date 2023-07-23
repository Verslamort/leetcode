# 删除序列相同元素并保持顺序

# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):  # 元素为hashable才可以
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedup(items, key=None):  # 不可哈希，dict类型
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedup(b, key=lambda d: (d['x'], d['y']))))  # key参数指定一个函数，将序列元素转换成hashable类型
    print(list(dedup(b, key=lambda d: d['x'])))


