# sw5105
import sys
sys.stdin = open("/input/sample_input.txt", "r")


'''
13101
10101
10101
10101
10021
'''
def safe(x,y):
    return 0<=x<N and 0<=y<N and maze[x][y]!=1
def find(x,y):
    global result
    queue.append([x,y])
    visited[x][y]=True
    while queue:
        start_x, start_y = queue.pop(0)
        for i in range(4):
            new_x = start_x+dx[i]
            new_y = start_y+dy[i]
            if safe(new_x,new_y) and not visited[new_x][new_y]:
                queue.append([new_x,new_y])
                visited[new_x][new_y]=True
                distance[new_x][new_y]=distance[start_x][start_y]+1
                if maze[new_x][new_y]==3 :
                    result = distance[new_x][new_y]-1
                    return

TC = int(input())
for test_case in range(1,TC+1):
    N = int(input())
    maze = [list(map(int,input())) for i in range(N)]
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                start_x , start_y = x,y
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = []
    visited = [[False]*N for i in range(N)]
    distance = [[0]*N for i in range(N)]
    result=0;
    find(start_x,start_y)
    print(result)


'''
def IsSafe(y,x):
    return 0 <= y < N and 0<= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)


def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            NewY = start_y + dy[dir]
            NewX = start_x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                Q.append((NewY, NewX))
                visited.append((NewY, NewX))
                Distance[NewY][NewX] = Distance[start_y][start_x] +1
                if Maze[NewY][NewX] == 3:
                    D_result = Distance[NewY][NewX] -1
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    D_result = 0
    Q = []
    Distance = [[0]*N for _ in range(N)]
    BFS(start_y, start_x)
    print(f'#{tc} {D_result}')
'''