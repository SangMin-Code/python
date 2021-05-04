# 3190.py
import sys
from typing import List

sys.stdin = open('input/3190')
import collections

def my(N:int, apples:List[List[int]],dirs:List[List[int]])->int:
    head = [1,1]
    tail = collections.deque()
    tail_length = 1
    move_dir = [[0,1],[1,0],[0,-1],[-1,0]]
    move_idx=0
    dir_dic = collections.defaultdict(int)
    for i,s in dirs:
        dir_dic[int(i)]=s

    for t in range(1,10000+1):
        #head 이동
        head = [head[0]+move_dir[move_idx][0],head[1]+move_dir[move_idx][1]]
        #사과가 있을 때 -> tail길이 추가
        if head in apples:
            tail.append(head)
            tail_length+=1
            apples.remove(head)
        #사과가 없을 때 ->  종료 조건 확인,tail 위치 이동
        else :
            if head in tail or head[0]==N+1 or head[1]==N+1 \
                            or head[0]==0 or head[1]==0:
                return t
            tail.append(head)
            if len(tail)>tail_length:
                tail.popleft()
        # 방향전환
        if dir_dic[t] == 'D':
            move_idx = (move_idx + 1) % 4
        elif dir_dic[t] == 'L':
            idx = move_idx - 1
            if idx < 0:
                move_idx = idx + 4
            else:
                move_idx = (idx) % 4

TC = int(input())
for test_case in range(1, TC+1):
    N = int(sys.stdin.readline().rstrip())
    apple_cnt = int(sys.stdin.readline().rstrip())
    apples=[list(map(int,sys.stdin.readline().rstrip().split())) for i in range(apple_cnt)]
    dir_cnt = int(sys.stdin.readline().rstrip())
    dirs = [list(sys.stdin.readline().rstrip().split()) for i in range(dir_cnt)]
    answer = my(N,apples,dirs)
    print(answer)
