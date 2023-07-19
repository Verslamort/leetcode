# 最大的k个数
import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []
        hp = arr[:k]
        heapq.heapify(hp)  # 生成最小堆
        for i in range(k, len(arr)):
            if hp[0] < arr[i]:
                heapq.heapreplace(hp, arr[i])
        return hp


if __name__ == '__main__':
    a = [4, 5, 1, 6, 2, 7, 3, 8]
    res = Solution().getLeastNumbers(a, 3)
    print(res)
