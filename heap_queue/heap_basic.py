import heapq


# 数组转化堆
heap = [1, 3, 4, 2, 6, 8, 9]
heapq.heapify(heap)
print(heap)
print('-----')

# 增加元素
heap = [1, 3, 4, 2, 6, 8, 9]
heapq.heappush(heap, 2)
print(heap)
print('-----')

# 删除堆顶
heap = [1, 3, 4, 2, 6, 8, 9]
heapq.heappop(heap)
print(heap)
print('-----')

# 删除堆顶，添加新值
heap = [1, 3, 4, 2, 6, 8, 9]
heapq.heapreplace(heap, 4)
print(heap)
print('-----')

# 查询堆中最大的n个数
heap = [1, 3, 4, 2, 6, 8, 9]
result = heapq.nlargest(2, heap)
print(result)
print('-----')

# 查询堆中最小的n个数
heap = [1, 3, 4, 2, 6, 8, 9]
result = heapq.nsmallest(3, heap)
print(result)
