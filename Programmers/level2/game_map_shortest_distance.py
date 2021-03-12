#game_map_shortest_distance.py
#https://programmers.co.kr/learn/courses/30/lessons/1844
import sys
sys.stdin=open('input/game_map_shortest_distance')
from typing import List
import collections

def my(maps:List[List[int]])->int:
    queue = collections.deque()
    queue.append([0, 0, 1])
    n, m, val = len(maps), len(maps[0]), []
    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while queue:
       x, y, cnt = queue.popleft()
       maps[x][y] = 0
       for dx, dy in d:
           nx, ny = x + dx, y + dy
           if nx== n - 1 and ny == m - 1:
               return cnt + 1
           elif n>nx>=0 and m>ny>=0 and maps[nx][ny] == 1:
               queue.append([nx, ny, cnt + 1])
    return -1

    '''
        queue = collections.deque()
        queue.append([0,0,1])
        n,m,val = len(maps),len(maps[0]),[]
        d = [[0,1],[1,0],[-1,0],[0,-1]]
        visited =   [[False]*m for _ in range(n)]
        can = False
        while queue:
            x,y,cnt = queue.popleft()
            maps[x][y]=0
            for dx,dy in d:
                if x+dx >=0 and x+dx <n \
                    and y+dy >=0 and y+dy <m \
                    and maps[x+dx][y+dy]!=0:
                    queue.append([x+dx,y+dy,cnt+1])
                    maps[x+dx][y+dy]=0
                    if x+dx == n-1 and y+dy ==m-1:
                        return cnt+1
        return -1
        '''

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    maps = []
    for _ in range(n):
        maps.append(list(map(int,input().split())))
    answer =my(maps)
    print(answer)