import sys
sys.stdin = open('input/convert_sorted_array_to_binary_search_tree')
from typing import List
from CodingInterview.my_util.Util import Codec, TreeNode

def my(nodes:List[int])->TreeNode:
    if not nodes:
        return None
    sorted_list= sorted(nodes[:])
    mid = len(nodes)//2
    node = TreeNode(nodes[mid])
    node.left = my(nodes[:mid])
    node.right = my(nodes[mid+1:])
    return node

def sorted_array_to_BST(nums:List[int])->TreeNode:
    if not nums:
        return None
    mid = len(nums)//2
    node = TreeNode(nums[mid])
    node.left = sorted_array_to_BST(nums[:mid])
    node.right = sorted_array_to_BST(nums[mid+1:])
    return node


nodes = list(map(int,input().split()))
result =my(nodes)
codec = Codec()
codec.printTree(result)