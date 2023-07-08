# 最长回文子串
"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
"""


def longest(s):
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    longestSubStr = ''
    longestLen = 0
    for j in range(len(s)):
        for i in range(j+1):
            if j-i < 1:
                if s[i] == s[j]:
                    dp[i][j] = 1
                    if longestLen < j-i+1:
                        longestLen = j-i+1
                        longestSubStr = s[i:j+1]
            elif j-i >1:
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    if longestLen < j-i+1:
                        longestLen = j-i+1
                        longestSubStr = s[i:j+1]
    return longestLen, longestSubStr


if __name__ == '__main__':
    a = 'baba'
    print(longest(a))


