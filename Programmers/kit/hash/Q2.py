# Q2.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q2')


#phone_book ( 1~1000000)
#phone_number = (1~20)
def my(phone_book:List[str])->bool:
    phone_book.sort()
    l =len(phone_book)
    for i in range(l-1):
        for j in range(i+1,l):
            current, compare = phone_book[i],phone_book[j]
            if len(compare)>len(current) and current == compare[:len(current)]:
                return False
    return True

def my2(phone_book:List[str])->bool:
    dic = collections.defaultdict(int)

    for i in phone_book:
        dic[i]+=1

    for num in phone_book:
        temp = ''
        for str in num:
            temp+=str
            if temp != num and dic[temp]>0:
                return False
    return True


TC = int(input())
for test_case in range(1, TC + 1):
    phone_book = list(input().split())
    answer = my(phone_book)
    print(answer)
