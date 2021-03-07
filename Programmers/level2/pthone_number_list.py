#https://programmers.co.kr/learn/courses/30/lessons/42577

import sys
import collections
sys.stdin = open('input/phone_number_list')
from  typing import List

def my(phone_book:List[str])->bool:
    phone_book.sort(key=lambda x: len(x))
    for i, str in enumerate(phone_book):
        if str in [target[:len(str)] for target in phone_book[i + 1:]]:
            return False
    return True

def my2(phone_book:List[str])->bool:
    #더 긴 번호가 짧은 번호의 접두어가 될 수 없으므로 길이로 오름차순 정렬
    phone_book.sort(key=lambda x:len(x))
    for i,number in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(number):
                return True
    return False

def practice(phone_book:List[str])->bool:
    hash =collections.defaultdict(str)
    for phone in phone_book:
        hash[phone]=1
    for phone in phone_book:
        temp=''
        for str in phone:
            temp+=str
            if hash[temp]==1 and temp!=phone:
                return False
    return True

'''
번호가 다른 번호의 접두어가 되는지 여부
-> 길이를 오름차순으로 정렬 후 번호 길이만큼을 이후 번호들에서 추출, List 에서 찾음
'''


TC= int(input())
for test_case in range(1, TC+1):
    answer = my(list(input().split()))
    print(answer)