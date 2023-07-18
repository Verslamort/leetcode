# 最小堆实现

class MinHeap():
    # 初始化最小堆
    def __init__(self, maxSize=None):
        self.maxSize = maxSize  # 最小堆初始化数组长度
        self.array = [None] * maxSize
        self._count = 0  # 最小堆中元素个数

    def length(self):
        return self._count

    def show(self):
        if self._count <= 0:
            print('null')
        print(self.array[: self._count], end=', ')

    def isEmpty(self):
        if self._count <= 0:
            return True
        else:
            return False

    def add(self, value):
        # 增加元素
        if self._count >= self.maxSize:
            raise Exception('Full')
        self.array[self._count] = value
        self._shift_up(self._count)
        self._count += 1

    def _shift_up(self, index):
        # 比较结点与根节点的大小，较小的为根结点
        if index > 0:
            parent = (index - 1) // 2
            if self.array[parent] > self.array[index]:
                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                self._shift_up(parent)

    def extract(self):
        # 获取最小值，并更新数组
        if self._count <= 0:
            raise Exception('The array is Empty')
        value = self.array[0]
        self._count -= 1  # 更新数组的长度
        self.array[0] = self.array[self._count]  # 将最后一个结点放在前面
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        # 此时index 是根结点
        if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            # 左右节点都存在
            if left < self._count and right < self._count:
                left_val = self.array[left]
                right_val = self.array[right]
                index_val = self.array[index]
                # left 最小
                if min(left_val, right_val, index_val) == left_val:
                    self.array[index], self.array[left] = self.array[left], self.array[index]
                    self._shift_down(left)
                # right 最小
                if min(left_val, right_val, index_val) == right_val:
                    self.array[index], self.array[right] = self.array[right], self.array[index]
                    self._shift_down(right)

            # 左叶子结点存在
            if left < self._count < right and self.array[left] < self.array[index]:
                self.array[left], self.array[index] = self.array[index], self.array[left]
                self._shift_down(left)


if __name__ == '__main__':
    m = MinHeap(10)
    import numpy as np
    np.random.seed(123)
    num = np.random.randint(100, size=10)  # 创建随机的10个数
    print(m.length())
    for i in num:
        m.add(i)
    m.show()


