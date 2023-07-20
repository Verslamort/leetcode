# 相对名次
"""
给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：
名次第 1 的运动员获金牌 "Gold Medal" 。
名次第 2 的运动员获银牌 "Silver Medal" 。
名次第 3 的运动员获铜牌 "Bronze Medal" 。
从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。

示例1
输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。
"""


class Solution(object):
    def findRelativeRanks(self, score):
        sortedscore = sorted(score)
        sortedscore.reverse()  # 大 -> 小排列
        scoretorank = {}  # 设置字典，对应每个score和排名
        for i in range(len(sortedscore)):
            scoretorank[sortedscore[i]] = i + 1
        answer = []
        for i in range(len(score)):  # 前三名输出对应字符串
            if scoretorank[score[i]] == 1:
                answer.append("Gold Medal")
            elif scoretorank[score[i]] == 2:
                answer.append("Silver Medal")
            elif scoretorank[score[i]] == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(scoretorank[score[i]]))  # 输出对应排名字符串
        return answer


if __name__ == '__main__':
    score = [5, 4, 3, 2, 1]
    res = Solution().findRelativeRanks(score)
    print(res)
