# 12015.py
import sys
from typing import List
import bisect
sys.stdin = open('input/12015')


def my(n:int, nums:List[int])->int:
    D = [0]

    def search(num):
        left,right = 0, len(D)-1
        s =0
        if D[-1]<num:
            return len(D)
        while left<=right:
            mid = left + (right - left) // 2
            if D[mid] >= num:
                s = mid
                right = mid - 1
            else:
                left = mid + 1
        return s

    for i in nums:
        idx = search(i)
        if idx==len(D):
            D.append(i)
        else:
            if i<D[idx]:
                D[idx]=i

    return len(D)-1

def my2(n:int,nums:List[int])->int:
    dp = []
    for i in nums:
        k = bisect.bisect_left(dp, i)  # 자신이 들어갈 위치 k
        if len(dp) <= k:  # i가 가장 큰 숫자라면
            dp.append(i)
        else:
            dp[k] = i  # 자신보다 큰 수 중 최솟값과 대체
    return len(dp)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,nums)
    print(answer)
