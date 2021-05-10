# 1021.py
import sys
from typing import List

sys.stdin = open('input/1021')

# board에 1~N 범위의 숫자를 놓고 start지점으로부터 찾는 숫자가
# 왼쪽, 오른쪽을 전부 스캔하면서 둘 중 짧은 것을 찾은 뒤 board에서 pop하고
# start 위치를 수정, nums에 모든 숫자에 대해 실행

def my(N:int,n:int,nums:List[int])->int:
    answer = 0
    board = [i+1 for i in range(N)]
    start = 0
    left,right = -1,-1
    for i in nums:
        l =len(board)
        for j in range(0,l):
            right+=1
            if board[(start+j)%l]==i:
                break
        for j in range(0,l):
            left +=1
            if board[(start-j)%l]==i:
                break
        answer+=min(left,right)
        if left<right:
            start = (start-left)%l
        else :
            start = (start+right)%l
        left,right=-1,-1
        board.pop(start)
    return answer

def my2(N:int,n:int,nums:List[int])->int:
    board = [i for i in range(1,N+1)]
    answer = 0

    for i in nums:
        idx = board.index(i)
        answer +=min(len(board[idx:]),len(board[:idx]))
        board = board[idx+1:]+board[:idx]
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    N,n = map(int,sys.stdin.readline().rstrip().split())
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my2(N,n,nums)
    print(answer)
