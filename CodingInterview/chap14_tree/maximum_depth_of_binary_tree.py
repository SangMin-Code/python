import sys
sys.stdin = open('input/maximum_depth_of_binary_tree')
from typing import List
import collections

class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left_child = None
        self.right_child=None
def my(tree:List[str])->int:
    depth =1
    sum = 1
    while sum<len(tree):
        sum += 2**depth
        depth+=1
    return depth
def my2(root:TreeNode)->int:
    queue =collections.deque([root])
    depth = 1
    while queue:
        node = queue.popleft()
        if len(queue)==0:
            depth+=1
        if node:
            queue.append(node.left_child)
            queue.append(node.right_child)
    return depth

def my3(root:TreeNode)->int:
    answer = 1
    def dfs(root:TreeNode,depth:int):
        nonlocal answer
        if not root:
            if depth > answer :
                answer=depth
        else :
            dfs(root.left_child,depth+1)
            dfs(root.right_child,depth+1)
    dfs(root,0)
    return answer

def maxDepth(root:TreeNode)->int:
    queue= collections.deque([root])
    depth = 0
    while queue:
        depth+=1
        #큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left_child:
                queue.append(cur_root.left_child)
            if cur_root.right_child:
                queue.append(cur_root.right_child)
    return depth



root = TreeNode(3)
root.left_child=TreeNode(9)
sub = TreeNode(20)
sub.left_child=TreeNode(15)
sub.right_child=TreeNode(7)
root.right_child=sub

tree = input().split()
print(my3(root))
#maxDepth(root)