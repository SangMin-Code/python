import sys
sys.stdin = open('hackerRank/warm_up_challange/input/sales_by_match.txt')


def solution(array):
    cnt = 0
    while array:
        num = array[0]
        cnt += array.count(num)//2
        array = [i for i in array if i != num]
    return cnt



TC = int(input())
for i in range(TC):
    n = int(input())
    array = list(map(int,input().split()))
    result = solution(array)
    print(result)