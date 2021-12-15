import sys
sys.stdin = open('Programmers/level1/input/lottos.txt')


def solution(lottos, win_nums):
    answer = [lottos.count(0), 0]
    score = [6, 6, 5, 4, 3, 2, 1]
    for i in range(6):
        if lottos[i] in win_nums:
            answer[0] += 1
            answer[1] += 1
    answer = [score[answer[0]], score[answer[1]]]
    return answer


TC = int(input())
for i in range(TC):
    lottos = list(map(int, input().split()))
    win_nums = list(map(int, input().split()))
    print(solution(lottos, win_nums))
