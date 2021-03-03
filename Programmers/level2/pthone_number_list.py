#https://programmers.co.kr/learn/courses/30/lessons/42577

import sys
sys.stdin = open('input/phone_number_list')
from  typing import List

def my(phone_book:List[str])->bool:
    phone_book.sort(key=lambda x: len(x))
    for i, str in enumerate(phone_book):
        if str in [target[:len(str)] for target in phone_book[i + 1:]]:
            return False
    return False
'''
번호가 다른 번호의 접두어가 되는지 여부
-> 길이를 오름차순으로 정렬 후 번호 길이만큼을 이후 번호들에서 추출, List 에서 찾음
'''


TC= int(input())
for test_case in range(1, TC+1):
    answer = my(list(input().split()))
    print(answer)