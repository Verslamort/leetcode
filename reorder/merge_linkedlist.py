# 合并排序链表
"""
给定一个链表数组，每个链表都已经按升序排列。
请将所有链表合并到一个升序链表中，返回合并后的链表。
"""


class ListNode(object):
    """创建生成链表节点的类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 遍历
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        global num
        res = ListNode()
        re = res
        while list1 and list2:
            # l1, l2是否存在
            num1 = list1.val if list1 else 200
            num2 = list2.val if list2 else 200
            if num1 > num2:
                num = num2
                list2 = list2.next
            elif num1 <= num2:
                num = num1
                list1 = list1.next
            re.next = ListNode(num)
            re = re.next

        while not list1 and list2:
            re.next = ListNode(list2.val)
            list2 = list2.next
            re = re.next

        while not list2 and list1:
            re.next = ListNode(list1.val)
            list1 = list1.next
            re = re.next
        return res.next


if __name__ == '__main__':
    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))
    rel = Solution().mergeTwoLists(a, b)
    res = Solution().mergeTwoLists(rel, c)
    while res:
        print(res.val, end='')
        res = res.next
