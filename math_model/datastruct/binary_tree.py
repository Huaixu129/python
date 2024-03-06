from collections import deque


class TreeNode:
    """ 二叉树节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


# 初始化二叉树
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
# 构建引用指向（即指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
# 插入与删除节点
p = TreeNode(0)
# 在 n1 -> n2 中间插入节点 P
n1.left = p
p.left = n2
# 删除节点 P
n1.left = n2


# 广度优先遍历
def level_order(root: TreeNode | None) -> list[int]:
    """ 层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
    res.append(node.val)  # 保存节点值
    if node.left is not None:
        queue.append(node.left)  # 左子节点入队
    if node.right is not None:
        queue.append(node.right)  # 右子节点入队
    return res


# 深度优先遍历
def pre_order(root: TreeNode | None):
    """ 前序遍历"""
    if root is None:
        return
    # 初始化一个列表，用于保存遍历序列
    res = [root.val]
    # 访问优先级：根节点 -> 左子树 -> 右子树
    pre_order(root=root.left)
    pre_order(root=root.right)

    def in_order(root: TreeNode | None):
        """ 中序遍历"""

        if root is None:
            return
        # 访问优先级：左子树 -> 根节点 -> 右子树
        in_order(root=root.left)
        res.append(root.val)
        in_order(root=root.right)

    def post_order(root: TreeNode | None):
        """ 后序遍历"""

        if root is None:
            return
        # 访问优先级：左子树 -> 右子树 -> 根节点
        post_order(root=root.left)
        post_order(root=root.right)
        res.append(root.val)
