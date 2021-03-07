#https://programmers.co.kr/learn/courses/30/lessons/42746
import sys
sys.stdin = open('input/biggest_number')
from typing import List

#functools.cmp_to_key(comparator)

#time out
def my(numbers:List[int])->List[int]:
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if str(numbers[j+1])+str(numbers[j])>str(numbers[j])+str(numbers[j+1]):
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers

def my2(numbers:List[str])->str:
    print(numbers)
    numbers.sort(key= lambda x : x*3,reverse=True)
    return ''.join(numbers)

def practice(numbers:List[str])->str:
    numbers.sort(key=lambda x:x*3, reverse=True)
    return ''.join(numbers)


TC = int(input())
for test_case in range(1,TC+1):
    numbers = list(map(str,input().split()))

    answer = my2(numbers)
    print(answer)