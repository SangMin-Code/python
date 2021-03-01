from CodingInterview.my_util.Util import Codec, TreeNode
import sys
sys.stdin = open('input/balenced_binary_tree')
import collections

#str= list(input().split())

def my(root:TreeNode)->bool:
    answer =[True]
    def DFS(node:TreeNode):
        if not node :
            return 0
        left = DFS(node.left)
        right = DFS(node.right)
        if abs(left-right)>1:
            answer[0]=False
        return max(left,right)+1
    DFS(root)
    return answer[0]

def isBalanced(root:TreeNode)->bool:
    def check(root):
        if not root:
            return 0
        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1\
            or abs(left-right)>1:
            return -1
        return max(left,right)+1
    return check(root)!= -1

TC = int(input())
for test_case in range(1,TC+1):
    codec = Codec()
    root = codec.deserialize(input())
    #codec.printTree(root)
    print(my(root))


