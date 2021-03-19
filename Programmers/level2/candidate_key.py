#https://programmers.co.kr/learn/courses/30/lessons/42890
#candidate_key.py
import sys
sys.stdin=open('input/candidate_key')
from typing import List
import collections
import itertools

def my(relation:List[List[str]])->int:
    candidate = [i for i in range(len(relation[0]))]
    row = len(relation)
    col = len(relation[0])
    result = []

    def comb(n:int, nums:List[int]):
        result = []
        stack =[]
        prev_elements = nums[:]
        def DFS(elements):
            if len(stack)==n:
                result.append(stack[:])
            elif len(stack)<n:
                for i,v in enumerate(elements[:]):
                    stack.append(v)
                    DFS(elements[i+1:])
                    stack.pop()
        DFS(nums)
        return result

    for n in range(col):
        colmuns = [i for i in itertools.combinations(candidate,n+1)]
        for com in colmuns:
            check_set = set()
            for i in range(row):
                s =''
                for j in com:
                    s+=relation[i][j]
                check_set.add(s)
            if len(check_set)==row:
                if len(com)==1:
                    candidate.remove(com[0])
                result.append(com)

    for i,v in enumerate(result):
        for j,val in enumerate(result[i+1:]):
            if set(v).intersection(set(val))==set(v):
                result.remove(val)
    return len(result)










TC = int(input())
for test_case in range(1,TC+1):
    row,col = map(int,input().split())
    relation = []
    for _ in range(row):
        relation.append(input().split())
    answer = my(relation)
    print(answer)