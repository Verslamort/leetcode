# 二叉树遍历
# 迭代

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


class Solution:
    def preorderTraversal(self, root):
        result = []  # 存放结果
        stack = []  # 存放中间节点的栈
        while root != None or len(stack) != 0:  # 只有root和栈都为空时才算遍历完
            while root != None:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result

    def inorderTraversal(self, root):
        result = []
        stack = []
        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def postorderTraversal(self, root):
        result = []  # 存放结果的列表
        stack = []  # 存放中间结点的栈
        preAccess = None
        while root != None or len(stack) != 0:  # 只有root和栈都为空时才算遍历完
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right == None or root.right == preAccess:  # 如果没有右子结点或者右子节点已经被访问了，应该进行跟结点值的存储
                result.append(root.val)
                preAccess = root
                root = None  # root置为空，下个循环将直接出栈
            else:  # 如果由右子树，则将root转移到右边，像左子树一样处理右子树
                stack.append(root)
                root = root.right
        return result


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
    re = Solution().inorderTraversal(bst)
    r = Solution().postorderTraversal(bst)
    print(res)
    print(re)
    print(r)
