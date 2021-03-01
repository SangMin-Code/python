import sys
sys.stdin = open('input/binary_search_tree_to_greater_sum_tree')
from typing import List
from CodingInterview.my_util.Util import Codec, TreeNode

#TODO 이진탐색함수 자신보다 큰 값 더하기

def my():
    str = input()
    nodeList = list(str.split())
    nums = []
    for i in nodeList:
        if i.isdigit():
            nums.append(int(i))
    nums = sorted(nums)

    for i,j in enumerate(nodeList):
        if j.isdigit():
            nodeList[i]=sum(nums[nums.index(int(j)):])
            print(nums[nums.index(int(j)):])
    print(nodeList)


class solution:
    val :int = 0

    def bstToGst(self,root:TreeNode)->TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val +=root.value
            root.value = self.val
            self.bstToGst(root.left)
        return root

my()
codec = Codec()

#test = codec.deserialize(input())


