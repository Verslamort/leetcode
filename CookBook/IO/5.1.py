# 读写文本数据

# 你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。
with open('./1.txt', 'rt') as f:
    data = f.read()
    print(data)
with open('./1.txt', 'rt') as f:
    for line in f:
        print(line)


with open('./2.txt', 'wt') as f:
    f.write('a')
    f.write('b')

with open('./2.txt', 'wt') as f:
    print(line, file=f)


