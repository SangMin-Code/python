import os, sys
# 프로젝트 root를 import 참조 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname('c:/practice/python/CodingInterview/my_util'))))
from CodingInterview.my_util.Util import TreeNode
import collections


def my(tree1:TreeNode, tree2:TreeNode)->TreeNode:
    if tree1 and tree2 :
        node = TreeNode(tree1.value + tree2.value)
        node.left = my(tree1.left , tree2.left)
        node.right = my(tree1.right, tree2.right)
        return node
    else :
        return tree1 or tree2




tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left=TreeNode(5)
tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right=TreeNode(4)
tree2.right.right =TreeNode(7)


result = my(tree1,tree2)
queue = collections.deque([result])

while queue:
    node =queue.popleft()
    if node :
        print(node.value)
        queue.append(node.left)
        queue.append(node.right)
    









