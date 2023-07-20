# 拿硬币
"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。
"""


class Solution:
    def minCount(self, coins):
        return sum([(x+1)//2 for x in coins])  # (x+1)//2 单堆硬币最小次数


if __name__ == '__main__':
    coins = [4, 2, 1]
    res = Solution().minCount(coins)
    print(res)
