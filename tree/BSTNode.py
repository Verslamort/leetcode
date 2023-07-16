class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '<{}>'.format(self.val)
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


def preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

def print_tree(root):

    '''
    打印一棵二叉树，二叉树节点值为0~9 10个整数或者26个大小写英文字母
    使用/\模拟左右分支,如下所示
            e
         /     \
        c       g
       / \     / \
      b   d   f   h
     /
    a
    但是在打印满二叉树时，最多打印三层，对于深度为4的二叉树，存在节点冲突，无法打印
    '''
    if root is None:
        return
    # 基本思想：
    # 查询二叉树高度，预留足够的打印区域
    current = 4
    # 计算深度为depth的满二叉树需要的打印区域：叶子节点需要的打印区域，恰好为奇数
    # 同一个节点左右孩子间隔 3 个空格
    # 相邻节点至少间隔一个空格，
    max_word = 3 * (2 ** (current - 1)) - 1
    node_space = int(max_word / 2)  # 每一个节点前面的空格数
    # queue1和queue2用来存放节点以及节点打印时的位置
    # queue1：当前层
    # queue2：下一层
    queue1 = [[root, node_space + 1]]
    queue2 = []
    while queue1:
        # 使用i_position列表记录左右斜杠的位置
        i_position = []
        # 确定左右斜杠的位置
        # "/"比当前节点的位置少1
        # "\"比当前节点的位置多1
        for i in range(len(queue1)):
            node = queue1[i][0]  # 节点打印位置
            i_space = queue1[i][1] - 1  # 左右斜线打印位置
            # 对于根节点，左右各空出两个空格
            if node.val == root.val:
                i_space -= 2
            # 存储左斜线和左孩子
            if node.left is not None:
                i_position.append([i_space, '/'])
                queue2.append([node.left, i_space - 1])
            i_space += 2
            if node.val == root.val:
                i_space += 4
            # 存储右斜线和右孩子
            if node.right is not None:
                i_position.append([i_space, '\\'])
                queue2.append([node.right, i_space + 1])
        # 打印节点和左右斜杠
        # 打印节点
        if len(queue1) > 0:
            # 找到打印位置最远的节点的位置
            last_node = queue1[len(queue1) - 1][1]
            # 当前打印节点的数目
            index = 0
            for i in range(last_node + 1):
                # 打印节点
                if index < len(queue1) and i == queue1[index][1]:
                    print(queue1[index][0].val, end='')
                    index += 1
                else:
                    # 打印空格
                    print(' ', end='')
        print()
        # 打印左右斜杠
        index = 0
        if len(i_position) > 0:
            for i in range(i_position[len(i_position) - 1][0] + 1):
                if i == i_position[index][0]:
                    print(i_position[index][1], end='')
                    index += 1
                else:
                    print(' ', end='')
        print()
        # 更新queue1和queue2
        queue1 = []
        while queue2:
            queue1.append(queue2.pop(0))
        node_space -= 2


class Solution:
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


def new2():
    b5 = BSTNode(5)
    b2 = BSTNode(2)
    b5.left = b2
    b8 = BSTNode(8)
    b5.right = b8
    b7 = BSTNode(7)
    b8.right = b7
    b8.left = BSTNode(6)
    b1 = BSTNode(1)
    # b1.left = BSTNode(0)
    # b1.right = BSTNode(8)
    b4 = BSTNode(4)
    b2.left = b1

    b2.right = b4
    b3 = BSTNode(3)
    b4.left = b3
    print_tree(b5)
    # preorder(b5)
    res = Solution().inorderTraversal(b5)
    print(res)
    return b5


def travel_tree(root):
    """
    stack ....
    [5]
    pop 5
    stack = [2, 8]

    pop 8
    statck = [2]
    statck = [2, 1]
    statck = [2, 1, 4]


    :param root:
    :return:
    """
    stack = [root, ]
    while stack:
        print(stack)
        node = stack.pop()
        # print(node.val, end=' ')
        right = node.right
        left = node.left

        if left is not None:
            stack.append(left)
        if right is not None:
            stack.append(right)


if __name__ == '__main__':
    b5 = new2()
    print()
    travel_tree(b5)
