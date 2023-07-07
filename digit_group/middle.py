# 寻找数组的中心索引
class Solution:
    def pivotIndex(self, nums):
        idx = 0
        # left 记录当前下标左边元素的和， right记录右边的和+当前元素
        left, right = 0, sum(nums)

        while idx < len(nums):
            if left == right - nums[idx]:  # 找到了中心下标
                return idx
            else:
                left += nums[idx]  # 不满足条件时，下标继续向后移动
                right -= nums[idx]
                idx += 1

        return -1


if __name__ == '__main__':
    a = [1, 7, 3, 6, 5, 6]
    r = Solution().pivotIndex(a)
    print(r)
