# Q1.py
import itertools
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(numbers:str)->int:
    nums = [True]*10000000
    nums[0],nums[1]=False,False

    for i in range(2,int(len(nums)**0.5)+1,1):
        if nums[i]:
            for j in range(i+i,len(nums),i):
                nums[j]=False
    primes = [i for i,j in enumerate(nums) if nums[i]]

    answer =[]

    for i in range(len(numbers)):
        for j in itertools.permutations(numbers,i+1):
            found = int(''.join(j))
            if found not in answer and found in primes:
                answer.append(found)

    return len(answer)

def my2(numbers:str)->int:

    def is_prime(num):
        for i in range(2,int(num**0.5)+1,1):
            if num%i==0:
                return False
        return True

    answer = []

    for i in range(len(numbers)):
        for j in itertools.permutations(numbers,i+1):
            found = int(''.join(j))
            if found == 0 or found==1:
                continue
            if found not in answer and is_prime(found):
                answer.append(found)
    return len(answer)


TC = int(input())
for test_case in range(1, TC + 1):
    numbers = input()
    answer = my2(numbers)
    print(answer)
