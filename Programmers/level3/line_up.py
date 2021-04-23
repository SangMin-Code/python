#line_up
import sys
sys.stdin=open('input/line_up')
from typing import List
import math
def my(n:int,k:int)->List[int]:
    answer = []
    numberList = [i for i in range(1, n + 1)]

    while (n != 0):
        temp = math.factorial(n) // n  # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = k // temp
        k = k % temp
        if k == 0:
            answer.append(numberList.pop(index - 1))
        else:
            answer.append(numberList.pop(index))

        n -= 1

    return answer





TC = int(input())
for test_case in range(1,TC+1):
    n,k = map(int,input().split())
    answer = my(n,k)
    print(answer)