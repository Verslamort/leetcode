# 实现strStr()
"""
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果needle 不是 haystack 的一部分，则返回 -1 。
"""


class Solution:
    def strStr(self, haystack, needle):
        l1 = len(haystack)
        l2 = len(needle)
        if l1 < l2:  # needle长度大于haystack, 不是haystack的一部分
            return -1
        l = l1 - l2 + 1
        for i in range(l):  # 从索引0到索引l遍历长字符串，截取与待查找子串长度相同的子字符串
            if haystack[i:i+l2] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    res = Solution().strStr(haystack, needle)
    print(res)
