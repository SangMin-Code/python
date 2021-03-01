#maze.py
'''
00013
01110
21000
01111
00000
'''

def candidate(maze, x,y,list,visited):
    # position[x,y] x <n
    #print(visited)
    n = len(maze)
    if y+1<n and maze[x][y+1]!=1 and not visited[x][y+1]:
        list.append([x,y+1])
    if y-1>=0 and maze[x][y-1]!=1 and not visited[x][y-1]:
        list.append([x,y-1])
    if x-1>=0 and maze[x-1][y]!=1 and not visited[x-1][y]:
        list.append([x-1,y])
    if x+1<n and maze[x+1][y]!=1 and not visited[x+1][y]:
        list.append([x+1,y])

def find(maze, position,visited,answer):
    x= position[0]
    y= position[1]
    visited[x][y] = True
    print(x,y)
    if maze[x][y]==3 :
        answer = 1
    else :
        list =[]
        candidate(maze,x,y,list,visited)
        for i in list:
            find(maze,i,visited,answer)


visited = [ [False]*5 for i in range(5) ]

list =[[0,0,0,1,3]
     ,[0,1,1,1,0]
     ,[2,1,0,0,0]
     ,[0,1,1,1,1]
     ,[0,0,0,0,0]]

answer =0
find(list,[2,0],visited,answer)
if visited[0][4] ==True : answer =1
print(answer)




