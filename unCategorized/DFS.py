#DFS.py
'''
6 5
1 4
1 3
3 2
2 5
4 6
1 6 ?
'''

lineList = [[],[3,4],[3,5],[1,2],[1,6],[6,2],[4,5]]
visited = [False]*7
stack =[]

def DFS(visited,s,g):
    if s == g : return 1
    visited[s] = True
    while(s):
        w= check(visited, lineList[s])
        if w:
            stack.append(s)
        while(w):
            if w == g : return 1
            visited[w] = True
            stack.append(w)
            s= w
            w = check(visited,list[s])
        s = stack.pop()
    return 0


def check(visited, list):
    for i in range(len(list)):
        if visited[i] == False:
            return list[i]
    return

DFS(visited,1,6)
'''
def DFS(start):
    global result
    visited[start] = 1
    for next in range(1, v+1):
        if MyMap[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next)

TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    MyMap = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1

    start_node, end_node = map(int, input().split())
    result = 0
    DFS(start_node)
    print(f'#{tc} {result}')

v, e = map(int, input().split())
list = [[False]*(v+1) for i range(v+1)]
visited = [False]*(v+1)
for i in range(e):
    start, end = map(int, input().split())
    list[start][end]= True
    list[end][start]=True
startNode, endNode = mpa(int, input().split())
result = 0
DFS(startNode,endNode)

def DFS(start, goal):
    visited[start] = True
    for next in range(1,v+1):
        if list[start][next] and not visited[next]:
            if next == goal:
                return 1
            DFS(next,goal)
'''