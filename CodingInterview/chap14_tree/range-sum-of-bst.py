import sys
from CodingInterview.my_util.Util import TreeNode,Codec
sys.stdin = open('input/range_sum_of_bst')
import collections

def my(root:TreeNode,L:int, R:int)->int:
    queue = collections.deque([root])
    sum =0
    while queue:
        node = queue.popleft()
        if node:
            if int(node.value)>=L and int(node.value)<=R:
                sum+=int(node.value)
            queue.append(node.left)
            queue.append(node.right)
    print(sum)

def broot_force(root:TreeNode, L:int, R:int)->int:
    if not root:
        return 0
    return (root.value if L<=root.value<=R else 0)+\
           broot_force(root.left,L,R)+\
           broot_force(root.right,L,R)

def branch_prunning(root:TreeNode,L:int,R:int)->int:
    def dfs(node:TreeNode):
        if not node:
            return 0
        if node.value<L:
            return dfs(node.right)
        elif node.value>R:
            return dfs(node.left)
        return node.value+dfs(node.left)+dfs(node.right)
    return dfs(root)

def using_stack(root:TreeNode, L:int, R:int)->int:
    stack, sum = [root],0
    while stack:
        node = stack.pop()
        if node:
            if node.value>L:
                stack.append(node.left)
            if node.value<R:
                stack.append(node.right)
            if L<=node.value<=R:
                sum+=node.value
    return sum

def using_queue(root:TreeNode, L:int, R:int)->int:
    queue, sum = collections.deque([root]),0
    while queue:
        node= queue.popleft()
        if node:
            if node.value>L:
                queue.append(node.left)
            if node.value<R:
                queue.append(node.right)
            if L<=node.value<=R:
                sum+=node.value
    return sum

L = int(input())
R = int(input())
str= input()
codec = Codec()
root = codec.deserialize(str)
my(root,L,R)