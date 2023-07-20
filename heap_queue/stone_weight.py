# 最后一块石头的重量
"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：
如果x == y，那么两块石头都会被完全粉碎；
如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
"""
import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)  # 大顶堆
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)  # 删除两块最重的石头
            if a != b:
                heapq.heappush(stones, a-b)  # 插入最重两块石头之差
        return -stones[0] if stones else 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    res = Solution().lastStoneWeight(stones)
    print(res)
