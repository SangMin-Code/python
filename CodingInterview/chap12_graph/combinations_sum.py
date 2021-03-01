import sys
sys.stdin=open('input/combinations_sum')
from typing import List
import timeit

def my(target:int, candidates:List[int])->List[List[int]]:
    results = []
    nums = []
    def find(v:int):
        if sum(nums)==target and sorted(nums[:]) not in results :
            results.append(sorted(nums[:]))
        elif sum(nums)<target :
            for i in candidates:
                nums.append(v)
                find(i)
                nums.pop()
    for i in candidates:
        find(i)
    return results

def combinationsSum(candidates:List[int],target:int)->List[List[int]]:
    result =[]
    def dfs(csum,index,path):
        if csum<0:
            return
        if csum==0:
            result.append(path)
            return
        for i in range(index,len(candidates)):
            dfs(csum-candidates[i],i,path+[candidates[i]])
    dfs(target,0,[])
    return result

TC = int(input())

for test_case in range(1,TC+1):
    target = int(input())
    candidates = list(map(int, input().split()))
    #time=timeit.timeit(stmt='print(my(target,candidates))',setup='from __main__ import my,target,candidates',number=1)
    #print(time)
    print(combinationsSum(candidates,target))