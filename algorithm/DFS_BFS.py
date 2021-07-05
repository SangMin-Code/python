'''
#DFS
 reculsively
DFS(G,v)
    label v as discovered
    for all directed deges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            reculisively call DFS(G,w)
'''
graph ={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}

def reculsive_dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = reculsive_dfs(w,discovered)
    return discovered
'''
DFS
iterative
DFS-iterative(G,v)
    let S be a stack
    S.push(v)
    while S in not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do
                S.push(w)
'''
def iterative_dfs(start_v):
    discovered = []
    stack =[start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

'''
BFS(G,start_v)
let Q be a queue
label start_v as discovered
Q.enqueue(start_v)
while Q is not empty do
    v:=Q.dequeue()
    if v is the goal then
        return v
    for all edges from v to w in G.adjacentEdges(v) do
        if w is not labeled as discovered then
        w.parent :=v
        Q.enqueue(w)
'''
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                queue.append(w)
                discovered.append(w)
    return discovered


