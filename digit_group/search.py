# 搜索插入位置
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)  # 采用左闭右开区间[left,right)
        while left < right:  # 右开所以不能有=,区间不存在
            mid = left + (right - left)//2
            if nums[mid] < target:  # 中点小于目标值,在右侧,可以得到相等位置
                left = mid + 1  # 左闭,所以要+1
            else:
                right = mid  # 右开,真正右端点为mid-1
        return left


if __name__ == '__main__':
    a = [1, 3, 8, 12, 32]
    b = 10
    res = Solution().searchInsert(a, b)
    print(res)

