# 从数量最多的堆取走礼物
"""
给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：
选择礼物数量最多的那一堆。
如果不止一堆都符合礼物数量最多，从中选择任一堆即可。
选中的那一堆留下平方根数量的礼物（向下取整），取走其他的礼物。
返回在 k 秒后剩下的礼物数量。
"""
import heapq
from math import isqrt


class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapq.heapify(gifts)  # 构建大顶堆
        while k and -gifts[0] > 1:
            heapq.heapreplace(gifts, -isqrt(-gifts[0]))  # isqrt  平方根向下取整
            k -= 1
        return -sum(gifts)


if __name__ == '__main__':
    gifts = [25, 64, 9, 4, 100]
    res = Solution().pickGifts(gifts, k=4)
    print(res)

