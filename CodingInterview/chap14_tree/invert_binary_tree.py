import collections

class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right=None


def my(root:TreeNode)->TreeNode:
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            left = node.left
        else :
            left = None
        if node.right :
            right = node.right
        else :
            right = None
        node.right = left
        node.left = right
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
    return root

def BFS(root:TreeNode)->TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.pop()
        if node :
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

def DFS(root:TreeNode)->TreeNode:
    stack = collections.deque([root])

    while queue:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

def post_order_DFS(root:TreeNode)->TreeNode:
    stack  = collections.deque([root])
    while queue:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)
            node.left, node.right = node.right, node.left

def pythonic(root:TreeNode)->TreeNode:
    if root:
        root.left, root.right=\
            pythonic(root.right),pythonic(root.left)
        return root
    return None





root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left=TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

node = my(root)
queue = collections.deque([node])
while queue:
    node= queue.popleft()
    print(node.value)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

