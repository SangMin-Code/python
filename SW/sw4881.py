#sw4881

import sys
sys.stdin = open("/input/sample_input.txt", "r")

def MyCalc(y):
    global sub_result, result
    if result < sub_result:
        return
    if y == N:
        if sub_result < result:
            result = sub_result
        return
    for x in range(N):
        if not visited[x]:
            visited[x] = True
            sub_result += lst[y][x]
            MyCalc(y+1)
            visited[x] = False
            sub_result -= lst[y][x]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 0, 987654321
    MyCalc(0)

    print(f'#{tc} {result}')

