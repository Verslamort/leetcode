# 合并区间
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])  # 按第一个元素从小到大排序
        new_list = []
        for i in intervals:
            # 把第一个数组元素添加到新数组
            if not new_list:
                new_list.append(i)
                continue

            # 如果有重合，就更新新的数组中的最后一个元素的最大值
            if new_list[-1][1] >= i[0]:
                x = max(new_list[-1][1], i[1])
                new_list[-1][1] = x
            else:
                # 如果没有重合，就直接添加到新的数组中
                new_list.append(i)

        return new_list


if __name__ == '__main__':
    a = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = Solution().merge(a)
    print(res)

