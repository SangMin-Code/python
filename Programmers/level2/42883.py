#큰 수 만들기 k개의 숫자를 빼서 만들 수 있는 숫자 중 가장 큰 수
import sys
sys.stdin = open('input/42883')

def my(k:int, strs:str)->str:
    nums = [num for num in strs]
    results = []
    prev_elements = []
    def dfs(elements):
        if len(prev_elements) == len(nums)-k:
            results.append(''.join(prev_elements[:]))
        for i,e in enumerate(elements):
            next_elements = elements[i:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return max(results)

TC = int(input())
for test_case in range(1, TC+1):
    k = int(input())
    strs = input()
    answer =my(k,strs)
    print(answer)