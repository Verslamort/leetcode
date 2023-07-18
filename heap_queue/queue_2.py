from queue import Queue   # 队列，FIFO
from queue import PriorityQueue  # 优先队列，优先级高的先输出


q = Queue(5) 	# 构建一个队列对象，maxsize初始化默认为零，此时队列无穷大
q.empty()		# 判断队列是否为空(取数据之前要判断一下)
q.full()		# 判断队列是否满了
q.put(1)		# 向队列存放数据
q.put(3)
q.put(2)
q.get()			# 从队列取数据
q.qsize()		# 获取队列大小，可用于判断是否满/空


q = PriorityQueue()
q.put((2, "Lisa"))
q.put((1, "Lucy"))
q.put((0, "Tom"))
i = 0
while i < q.qsize():
    print(q.get())
