import sys
sys.stdin = open('hackerRank/medium/input/find_minimum_number_of_fountain.txt')


def solution(fountains):

    N = len(fountains)
    dp = [-1]*N

    for idx, f in enumerate(fountains):
        left = max(0, idx-f)
        right = min(N, idx+f+1)
        dp[left] = max(right, dp[left])

    cnt = 1
    next_idx = 0
    right_idx = dp[0]

    for i in range(N):
        next_idx = max(next_idx, dp[i])
        if(i == right_idx):
            cnt += 1
            right_idx = next_idx
    return cnt


TC = int(input())
for i in range(TC):
    fountains = list(map(int, input().split()))
    result = solution(fountains)
    print(result)
