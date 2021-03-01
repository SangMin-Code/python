from typing import List



class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right=None

def my (root:TreeNode)->int:
    pass

class solution:
    logest :int = 0

    def diameterOfBinaryTree(self,root:TreeNode)->int:
        def dfs(node:TreeNode)->int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.logest = max(self.logest, left+right+2)
            return max(left,right)+1
        dfs(root)
        return self.logest



root = TreeNode(1)
root.righ=TreeNode(3)
sub = TreeNode(2)
sub.left=TreeNode(4)
sub.right=TreeNode(5)
root.left=sub


#my(root)
x= solution.diameterOfBinaryTree(root)
print(x)