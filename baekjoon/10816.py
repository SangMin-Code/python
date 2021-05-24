# 10816.py
import collections
import sys
from typing import List

sys.stdin = open('input/10816')


def my(list_a:List[int],list_b:List[int])->List[str]:

    cnt_list = collections.Counter(list_a)

    answer = [""]*len(list_b)

    for i in range(len(list_b)):
        answer[i] = str(cnt_list[list_b[i]])

    return answer

def my2(list_a:List[int],list_b:List[int])->List[str]:

    list_a.sort()

    def binary_left(n):
        start,end,mid =0, len(list_b)-1,(len(list_b)-1)//2
        while True:
            mid = start + (end-start)//2
            if start>end:
                if list_a[start]==n:
                    return start
                else :
                    return 0
            if list_a[mid]>=n:
                end = mid-1
            else :
                start = mid+1

    def binary_right(n):
        start, end, mid = 0, len(list_b) - 1, (len(list_b) - 1) // 2
        while True:
            mid = start + (end - start) // 2
            if start > end:
                if list_a[end]==n:
                    return end
                else:
                    return 0
            if list_a[mid] <= n:
                start = mid +1
            else:
                end = mid - 1
    answer = [""] * len(list_b)

    for idx,i in enumerate(list_b):
        answer[idx]= str(binary_right(i)-binary_left(i)+1)
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    list_a = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    list_b = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = my2(list_a, list_b)
    print(' '.join(answer))
