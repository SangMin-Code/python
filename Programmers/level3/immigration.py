#immigration
import sys
sys.stdin=open('input/immigration')
from typing import List

def my(n:int, times:List)->int:
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid // time
            # 심사 인원수를 넘으면 다음 단계
            if count >= n: break

        # n명을 심사 할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다.
        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    times = list(map(int,input().split()))
    answer = my(n,times)
    print(answer)