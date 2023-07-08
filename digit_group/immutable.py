# 字符串最长公共前缀
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


def longest(list_1):
    list_2 = []
    if len(list_1) == 0:
        return ''

    num = 0
    for k in list_1:  # 找到最短的长度， 来作为最长公共前缀的最长长度
        if len(k) > num:
            num = len(k)

    for i in range(num):  # i为索引
        for j in list_1:  # 将每个子字符串的第i个字母添加到列表
            list_2.append(j[i])
        if len(set(list_2)) == 1:  # 集合去除重复字母
            list_2.clear()
        else:
            if j[0: i: 1]:
                return j[0: i: 1]
            else:
                return ''


if __name__ == '__main__':
    a = ["flower", "flow", "flight"]
    print(longest(a))
    print('-----')
    b = ["dog", "racecar", "car"]
    print(longest(b))
