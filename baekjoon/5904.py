# 5904.py
import collections
import sys
from typing import List

sys.stdin = open('input/5904')


def my(n:int)->str:
    s="moo"
    k=1
    while len(s)<n:
        s = s+"m"+"o"*(k+2)+s
        k+=1
    return s[n-1]

def my2(n:int)->str:
    dic = collections.defaultdict(list)
    l= 3
    k= 0
    dic[0]=[1]

    while l<n:
        k += 1
        l = 2*l+k+3
        dic[k]=dic[k-1]+[l+1]+[i+l+k+3 for i in dic[k-1]]

    if n in dic[k]:
        return "m"
    else :
        return "o"
def my3(n:int)->str:
    k,l =0,0
    dic = collections.defaultdict(int)
    while l<n:
        l=2*l+k+3
        dic[k]=l
        k+=1

    def dfs(idx,k):
        print(idx,k)
        if k ==0:
            if idx==1:
                return "m"
            else :
                return "o"
        elif k>0 :
            if idx<=dic[k-1]:
                return dfs(idx,k-1)
            elif idx>dic[k-1]+k+3:
                return dfs(idx-dic[k-1]-k-3,k-1)
            elif idx == dic[k-1]+1:
                return "m"
            else :
                return "o"

    return dfs(n,k)

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    answer = my3(n)
    print(answer)
