# 数据流中第k大的元素
"""
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
请实现 KthLargest 类：
KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
"""


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.nums.sort()

    # 二分插入
    def add(self, val):
        left = 0
        right = len(self.nums)
        idx = (left + right) // 2
        while left < right:
            if val < self.nums[idx]:
                right = idx
            elif val > self.nums[idx]:
                left = idx + 1
            else:
                break
            idx = (left + right) // 2
        self.nums.insert(idx, val)
        return self.nums[-self.k]


if __name__ == '__main__':
    a = KthLargest(3, [4, 5, 8, 2])
    print(a.add(12))
