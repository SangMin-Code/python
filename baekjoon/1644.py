# 1644.py
import sys
from typing import List

sys.stdin = open('input/1644')

def my(N:int)->int:
    primes = [True for _ in range(4000001)]
    for i in range(2,int(4000001**0.5)+1):
        if primes[i]:
            for j in range(i+i,4000001,i):
                primes[j]=False

    prime_list = [i for i,j in enumerate(primes) if j and i>=2]

    sum_prime = [0]*(len(prime_list)+1)
    for i in range(len(prime_list)):
        sum_prime[i+1] = sum_prime[i]+prime_list[i]

    answer,start,end = 0,0,1

    while start < len(sum_prime) and prime_list[end-1]<=N:
        if sum_prime[end]-sum_prime[start]==N:
            answer+=1
            start+=1
        elif sum_prime[end]-sum_prime[start]>N:
            start+=1
        else :
            if end<len(sum_prime)-1:
                end+=1
            else:
                start+=1
    return answer

def my2(N:int)->int:
    #소수
    primes = [True for _ in range(4000001)]
    for i in range(2,int(4000001**0.5)+1):
        if primes[i]:
            for j in range(i+i,4000001,i):
                primes[j]=False

    prime_list = [i for i,j in enumerate(primes) if j and i >=2]

    answer,left,right = 0, 0, 1

    while left<len(prime_list) and prime_list[right-1]<=N:
        prime_sum = sum(prime_list[left:right])
        if prime_sum >= N:
            left +=1
            right = left+1
            if prime_sum ==N:
                answer+=1
        else :
            if right < len(prime_list):
                right+=1
            else:
                left+=1
                right = left+1
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    answer = my2(N)
    print(answer)
