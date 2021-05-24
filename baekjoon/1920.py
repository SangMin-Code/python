# 1920.py
import bisect
import sys
from typing import List

sys.stdin = open('input/1920')


def my(list_a:List[int],list_b:List[int])->List[int]:
    list_a.sort()
    answer=[]
    for i in list_b:
        result = bisect.bisect_left(list_a,i)
        if result !=len(list_a) and list_a[result]==i:
            answer.append(1)
        else:
            answer.append(0)
    return answer

def my2(list_a:List[int],list_b:List[int])->List[int]:
    list_a.sort()
    answer = [0]*len(list_b)

    def binary_serach(start,end,num):
        if start <= end:
            mid = start + (end-start)//2
            if list_a[mid]==num:
                return 1
            elif list_a[mid]<num:
                return binary_serach(mid+1,end,num)
            else :
                return binary_serach(start,mid-1,num)
        else :
            return 0

    for i in range(len(list_b)):
        answer[i] = binary_serach(0,len(list_a)-1,list_b[i])

    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    list_a  = list(map(int,sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    list_b  = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my2(list_a,list_b)
    for i in answer:
        print(i)
