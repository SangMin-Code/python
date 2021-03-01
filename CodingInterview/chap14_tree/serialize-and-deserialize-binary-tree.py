
from CodingInterview.my_util.Util import TreeNode
from typing import List
import collections


def my(serial:List[str], root:TreeNode):
    queue = collections.deque([root])
    nums = []
    while queue:
        node =queue.popleft()
        if node :
            nums.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else :
            nums.append('null')

    temp = [ i for i in nums if i !='null' ]
    nums = nums[:nums.index(temp[-1])+1]
    print(nums)

def serialize(root:TreeNode)->str:
    queue = collections.deque([root])
    result = ['#']
    #트리 BFS 직렬화
    while queue:
        node = queue.popleft()
        if node :
            queue.append(node.left)
            queue.append(node.right)
            result.append(str(node.value))
        else :
            result.append('#')
    return ' '.join(result)

def deserialize(data:str)->TreeNode:
    #예외 처리
    if data == '# #':
        return None
    nodes = data.split()

    root = TreeNode(int(nodes[1]))
    queue = collections.deque([root])
    index = 2
    while queue:
        node = queue.popleft()
        if nodes[index] is not '#':
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)
        index+=1
        if nodes[index] is not '#':
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index+=1
    return root


serial = ['1','2','3','null','null','4','5']
root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)

my(serial,root)

