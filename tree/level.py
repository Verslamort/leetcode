# 二叉树层序遍历


class BSTNode:
    """
    二叉树的节点
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        else:
            if self.right is not None:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)


class Solution:
    def levelOrder(self, root):
        if not root:
            return
        queue = [root]
        list1 = []
        while queue:
            list2 = []
            for i in range(len(queue)):
                a = queue.pop(0)  # 元素出队列
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                list2.append(a.val)
            list1.append(list2)
        return list1


if __name__ == '__main__':
    bst = BSTNode(52)
    bst.insert(50)
    bst.insert(20)
    bst.insert(53)
    bst.insert(11)
    bst.insert(22)
    bst.insert(52)
    bst.insert(78)
    res = Solution().levelOrder(bst)
    print(res)
