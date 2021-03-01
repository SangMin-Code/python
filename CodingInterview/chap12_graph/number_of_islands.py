#number_of_islands
import sys
sys.stdin = open('input/number_of_islands')
from typing import List

def find(grid:List[List[str]],i:int, j:int):
    if i <0 or i>=len(grid)\
       or j<0 or j>=len(grid[0])\
       or grid[i][j]!='1':
        return
    grid[i][j]='0'

    find(grid,i+1,j)
    find(grid,i-1,j)
    find(grid,i,j+1)
    find(grid,i,j-1)
def my(grid:List[List[str]])->int:
    count =0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                find(grid,i,j)
                count+=1
    return count

def numIslands(grid:List[List[str]])->int:
    def dfs(i,j):
        if i<0 or i>=len(grid) or \
           j<0 or j>=len(grid[0]) or \
            grid[i][j]!='1':
                return

        grid[i][j]=0
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                dfs(i,j)
                count+=1
    return count

TC =int(input())
for test_case in range(1,TC+1):
    n = int(input())
    islands = []
    for _ in range(n):
        t= input()
        t_list = []
        for str in t :
            t_list.append(str)
        islands.append(t_list)
    print(my(islands))