#longest_univalue_path
#TODO 트리 백트래킹
import collections

class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right=None

class my:
    longest :int=0
    def diameterOfBinaryTree(self,root:TreeNode)->int:
        def dfs(node:TreeNode)->int:
            if not node:
                return -1
            if node.left and node.value == node.left.value:
                left = dfs(node.left)
            else :
                left = dfs(None)
            if node.right and node.value == node.right.value:
                right = dfs(node.right)
            else :
                right = dfs(None)
            self.longest = max(self.longest,left+right+2)
            return max(left,right)+1
        queue = collections.deque([root])
        while queue:
            node =queue.popleft()
            dfs(node)
            if node.left :
                queue.append(node.left)
            if node. right:
                queue.append(node.right)
        return self.longest

class Solution:
    result : int = 0

    def longest_univalue_path(self,root:TreeNode)->int:
        def dfs(node:TreeNode):
            if node is None:
                return 0
            #존재하지 않는 노드까지 DFS 재귀탐색
            left = dfs(node.left)
            right = dfs(node.right)

            #현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.value == node.value:
                left+=1
            else :
                left =0
            if node.right and node.right.value == node.value:
                right+=1
            else :
                right =0
            #왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result,left+right)
            #자식 노드 상태값 중 큰 값 리턴
            return max(left,right)
        dfs(root)
        return self.result


root = TreeNode(1)
root.left = TreeNode(1)
root.left.left=TreeNode(1)
root.left.right = TreeNode(1)
root.right= TreeNode(1)
root.right.right=TreeNode(1)

solution = my()
answer = solution.diameterOfBinaryTree(root)
print(answer)