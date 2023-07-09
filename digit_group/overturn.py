# 翻转字符串里的单词
"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
"""


class Solution:
    def reverseWords(self, s):
        s = s.strip()
        i = j = len(s)-1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':  # 搜索首个空格
                i -= 1
            res.append(s[i+1:j+1])  # 添加单词
            while s[i] == ' ':  # 跳过单词间空格
                i -= 1
            j = i  # 指向下个单词尾字符
        return ' '.join(res)


if __name__ == '__main__':
    a = 'the sky is blue'
    b = 'hello world'
    c = ' hello world '
    r = Solution().reverseWords(a)
    re = Solution().reverseWords(b)
    res = Solution().reverseWords(b)
    print(r)
    print(re)
    print(res)
