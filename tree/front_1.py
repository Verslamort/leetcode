# 二叉树遍历
# 递归

class BSTNode:
    """
    二叉树的节点
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        # 给 bst 新增一个值
        # 新增值就要看值
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


# 前序遍历
class Solution:
    def preorderTraversal(self, root):
        result = []
        self.accessTree(root, result)
        return result

    def accessTree(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.accessTree(root.left, result)
        self.accessTree(root.right, result)


# 中序遍历
class Solute:
    def inorderTraversal(self, root):
        result = []
        self.accessTree(root, result)
        return result

    def accessTree(self, root, result):
        if root == None:
            return
        self.accessTree(root.left, result)
        result.append(root.val)
        self.accessTree(root.right, result)


# 后序遍历
class Solu:
    def postorderTraversal(self, root):
        result = []
        self.accessTree(root, result)
        return result

    def accessTree(self, root, result):
        if root == None:
            return
        self.accessTree(root.left, result)
        self.accessTree(root.right, result)
        result.append(root.val)


if __name__ == '__main__':
    bst = BSTNode(52)
    bst.insert(50)
    bst.insert(20)
    bst.insert(53)
    bst.insert(11)
    bst.insert(22)
    bst.insert(52)
    bst.insert(78)
    res = Solution().preorderTraversal(bst)
    print(res)
    re = Solute().inorderTraversal(bst)
    print(re)
    r = Solu().postorderTraversal(bst)
    print(r)
