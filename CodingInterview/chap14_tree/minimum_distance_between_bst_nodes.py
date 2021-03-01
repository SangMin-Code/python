from CodingInterview.chap12_graph.permutations import reculsion
from CodingInterview.my_util.Util import Codec,TreeNode
import sys
sys.stdin = open('input/minimum_distance_between_bst_nodes')

#TODO 중위순회

def my():
    pass

class solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def reculsion(self,root:TreeNode)->int:
        if root.left:
            reculsion(root.left)
        self.result = min(self.result, root.value-self.prev)
        self.prev = root.value
        if root.right:
            reculsion(root.right)
        return self.result

    def using_stack(self,root:TreeNode)->int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node= root
        while stack or node:
            while node:
                stack.append(node)
                node= node.left
            node = stack.pop()
            result = min(result, node.value-prev)
            prev = node.value
            node = node.right
        return result



TC = int(input())
for test_case in range(1,TC+1):
    str = input()
    codec = Codec()
    root = codec.deserialize(str)


