import sys
import itertools
from typing import List
sys.stdin = open('Programmers/level2/input/fatigue.txt')


def solution(k: int, dungeons: List[List[int]]) -> int:
    result = 0
    visited = [False]*len(dungeons)

    def DFS(visited, remain, cnt, dungeons):
        result = cnt
        for next_i, next_dungeon in enumerate(dungeons):
            if not visited[next_i] and next_dungeon[0] <= remain:
                next_visited = visited[:]
                next_visited[next_i] = True
                result = max(result, DFS(
                    next_visited, remain-next_dungeon[1], cnt+1, dungeons))
        return result

    for idx, dungeon in enumerate(dungeons):
        if dungeon[0] <= k:
            visited[idx] = True
            result = max(result, DFS(visited, k-dungeon[1], 1, dungeons))
            visited[idx] = False

    return result


def solution2(k, dungeons):
    answer = -1
    visited = 0
    for dungeon_p in itertools.permutations(dungeons):
        remain, count = k, 0
        for need, use in dungeon_p:
            if remain >= need:
                remain -= use
                count += 1
        visited = max(visited, count)
    answer = visited
    return answer


TC = int(input())
for i in range(TC):
    k = int(input())
    dungeons = [list(map(int, i.split())) for i in input().split(',')]
    # result = solution(k, dungeons)
    result = solution2(k, dungeons)
    print(result)
