import sys
sys.stdin = open('input/combinations')
from typing import List
import itertools

def my(n:int, k:int)->List[int]:
    nums = [i for i in range(1,n+1)]
    results = []
    prev_elements = []
    def dfs(elements):
        if len(prev_elements) ==k and sorted(prev_elements[:]) not in results :
            results.append(sorted(prev_elements[:]))
        elif len(prev_elements) <k:
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                #print(prev_elements)
                dfs(next_elements)
                prev_elements.pop()
    dfs(nums)
    return results

def combination(n:int, k:int)->List[List[int]]:
    results = []
    def dfs(elements, start:int, k:int):
        if k ==0:
            results.append(elements[:])
        for i in range(start,n+1):
            elements.append(i)
            dfs(elements,i+1,k-1)
            elements.pop()
    dfs([],1,k)
    return results

def using_itertools(n:int, k:int)->List[List[int]]:
    return list(itertools.combinations(range(1,n+1),k))


def using_generator(n, k):
    array = [i for i in range(1,n+1)]
    result = []
    for i in range(1,len(array)):
        if k == 0: # 종료 조건
            yield [array[i]]
        else:
            for next in using_generator(array[i+1:], k-1):
                yield [array[i]] + next

n = int(input())
k=int(input())
print(my(n,k))
print(combination(n,k))
print(using_itertools(n,k))

