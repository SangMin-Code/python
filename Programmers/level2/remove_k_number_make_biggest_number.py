import sys
sys.stdin = open('input/remove_k_number_make_biggest_number')
from typing import List
import itertools
#https://programmers.co.kr/learn/courses/30/lessons/42883
def my(numbers:str,k:int)->str:
    # len(number) 진행하면서 뒤에 더 큰 숫자 있는지 판별,
    # len-k-n 길이 이상인지 확인 후 i 번째 숫자 제거
    answer = ''
    for i,v in enumerate(numbers):
        idx = -1
        for j in range(i+1,len(numbers)):
            if numbers[j]>v:
                idx = j
                break
        if idx!=-1 and len(numbers)-idx>=len(numbers)-k-len(answer):
            continue
        else :
            answer += v
    return answer
    #timeout

def my2(number:str, k:int)->str:
    stack = [number[0]]
    for i, v in enumerate(number[1:], 1):
        while stack and v > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += number[i:]
            break
        stack.append(v)
    stack = stack[:-k] if k > 0 else stack
    answer = ''.join(stack)

def prcatice(number:str, k:int)->str:
    stack = [number[0]]
    for i,v in enumerate(number[1:],1):
        while stack and v>stack[-1] and k>0:
            stack.pop()
            k-=1
        if k ==0:
            stack+=number[i:]
            break
        stack.append(v)
    stack = stack[:-k] if k>0 else stack
    answer = ''.join(stack)

def practice_permutation(number:str, k:int)->str:
    numbers = [i for i in range(len(number))]
    result =[]
    prev_list=[]
    l = len(numbers)-k
    def DFS(elements):
        if len(prev_list)==l:
            result.append(int(''.join(prev_list[:])))
        elif len(prev_list)<l :
            for e in elements:
                next_elements = numbers[e+1:]
                prev_list.append(number[e])
                DFS(next_elements)
                prev_list.pop()
    DFS(numbers)
    return str(max(result))

def using_itertools(number:str,k:int)->str:
    for_combination = itertools.combinations(list(map(int,number)),len(number)-k)
    temp = [''.join(map(str,i)) for i in for_combination]
    return max(temp)


TC = int(input())
for test_case in range(1,TC+1):
    k=int(input())
    numbers = input()
    #answer =my2(numbers,k)
    #answer = practice_permutation(numbers,k)
    answer = using_itertools(numbers,k)
    print(answer)