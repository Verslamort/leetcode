# 数组中两元素的最大乘积
"""
给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
请你计算并返回该式的最大值。
"""
from heapq import nlargest
from operator import mul


class Solution:
    def maxProduct(self, nums):
        return mul(*map(lambda x: x-1, nlargest(2, nums)))  # 查询堆中最大的两个数，各自-1然后相乘


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    res = Solution().maxProduct(nums)
    print(res)

