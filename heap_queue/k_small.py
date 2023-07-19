# 最小的k个数
import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]  # 生成大顶堆
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if arr[i] < -hp[0]:  # 弹出堆头，放入新数
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])

        res = [-x for x in hp]

        return res


if __name__ == '__main__':
    a = [4, 5, 1, 6, 2, 7, 3, 8]
    res = Solution().getLeastNumbers(a, 4)
    print(res)
