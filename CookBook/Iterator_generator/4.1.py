# 手动遍历迭代器

# 你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。
def manual_iter():
    with open('./1.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


manual_iter()

# 交互示例
items = [1, 2, 3]
# Get the iterator
it = iter(items)
print(next(it))
print(next(it))
print(next(it))




