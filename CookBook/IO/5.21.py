# 序列化Python对象
import math
import pickle


# 你需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它。
data = 'abcd'
f = open('./5_21.txt', 'wb')
pickle.dump(data, f)

# 将一个对象转储为一个字符串
s = pickle.dumps(data)
print(s)

# 从字节流中恢复一个对象
# 从文件还原
f = open('./5_21.txt', 'rb')
data = pickle.load(f)
# 从字符串还原
data = pickle.loads(s)


f = open('./5_21.txt', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('./5_21.txt', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))


print(pickle.dumps(math.cos))



