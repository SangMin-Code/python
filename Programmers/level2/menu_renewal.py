#menu_renewal.py
#https://programmers.co.kr/learn/courses/30/lessons/72411
import sys
sys.stdin=open('input/menu_renewal')
from typing import List
import collections
import itertools

def my(course:List[int],orders:List[str])->List[str]:
    strs =[]
    result = []
    def make_list(elements,n):
        if len(prev_elements)==n:
            candidiates.append(''.join(prev_elements[:]))
        elif len(prev_elements)<n:
            for i,str in enumerate(elements):
                next_elements = elements[i+1:]
                prev_elements.append(str)
                make_list(next_elements,n)
                prev_elements.pop()
    for i,str in enumerate(orders):
        new_str = []
        for j in str:
            if j not in strs:
                strs.append(j)
            new_str.append(j)
        new_str.sort()
        orders[i]=''.join(new_str)
    strs.sort()
    orders.sort()

    for num in course:
        max_num = 0
        dic = collections.defaultdict(int)
        prev_elements = []
        candidiates = []
        make_list(strs[:], num)
        for i in candidiates:
            cnt =0
            for j in orders:
                if len(j)>=num:
                    flag = True
                    for k in i:
                        if k not in j:
                            flag = False
                            break
                    if flag:
                        dic[i] = dic[i]+1
                        cnt+=1
            max_num = max(max_num,cnt)
        temp_list = []
        for i in dic:
            if dic[i]==max_num and max_num>1:
                temp_list.append(i)
        result.extend(temp_list)
        result.sort()
    return result

def my2(course:List[int],orders:List[str])->List[str]:
    result = []
    for numbers in course:
        candidates = []
        for order in orders:
            in_order = itertools.combinations(sorted(order), numbers)
            for i in in_order:
                candidates.append(''.join(i))
        num = collections.Counter(candidates)
        for i in num:
            if num[i] == num.most_common()[0][1] and num[i]>1:
                result.append(i)
    result.sort()
    return result

def practice(course:List[int],orders:List[str])->List[str]:
    result = []
    for number in course:
        candidate = []
        for order in orders:
            com = itertools.combinations(sorted(order),number)
            for i in com:
                candidate.append(''.join(i))
        num = collections.Counter(candidate)
        for i in num:
            if num[i] == num.most_common()[0][1] and num[i]>1:
                result.append(i)
    result.sort()
    return result

TC = int(input())
for test_case in range(1,TC+1):
    course = map(int,input().split())
    orders = input().split()
    answer =my2(course,orders)
    print(answer)
