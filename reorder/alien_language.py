# 外星语言是否排序
"""
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        def test(word_1, word_2, order):
            for i in range(len(word_1)):
                if i >= len(word_2):
                    return True
                if order.index(word_1[i]) > order.index(word_2[i]):
                    return True
                if order.index(word_1[i]) < order.index(word_2[i]):
                    return False

        for i in range(len(words)-1):
            if test(words[i], words[i+1], order):
                return False
        return True


if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    res = Solution().isAlienSorted(words, order)
    print(res)
