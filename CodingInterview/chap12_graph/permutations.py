import sys
sys.stdin = open('input/permutations')
from typing import List
import itertools


def my(nums:List[int])->List[List[int]]:
    answer = []
    search=[]
    def find(idx:int, v:int, search:List[int]):
        search.append(v)
        if idx == len(nums)-1:
            temp = search.copy()
            answer.append(search[:])
        else :
            for i in nums:
                if i not in search:
                    find(idx+1,i,search)
        #print(search)
        search.pop()
    for i in nums:
        find(0,i,search)
    print(answer)

def reculsion(nums:List[int])->List[List[int]]:
    results =[]
    prev_elements=[]
    def dfs(elements):
        if len(elements)==0:
            results.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
    dfs(nums)
    return results

def using_itertools(nums:List[int])->List[List[int]]:
    return list(itertools.permutations(nums))


nums = list(map(int,input().split()))
my(nums)