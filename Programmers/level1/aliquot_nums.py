import sys
sys.stdin = open('Programmers/level1/input/aliquot_nums.txt')


def solution(left: int, right: int) -> int:
    result = 0
    for num in range(left, right+1):
        if int(num**0.5)**2 == num:
            result -= num
        else:
            result += num
    return result


TC = int(input())
for i in range(TC):
    left, right = map(int, input().split())
    result = solution(left, right)
    print(result)
