# 煎饼排序
"""
给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
一次煎饼翻转的执行过程如下：
选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在10 * arr.length 范围内的有效答案都将被判断为正确。
"""


class Solution:
    def pancakeSort(self, arr):
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n-1:
                continue
            m = index
            for i in range((m+1)//2):
                arr[i], arr[m-i] = arr[m-i], arr[i]
            for i in range(n//2):
                arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
            ans.append(index+1)
            ans.append(n)
        return ans


if __name__ == '__main__':
    a = [3, 2, 1, 4]
    res = Solution().pancakeSort(a)
    print(res)
