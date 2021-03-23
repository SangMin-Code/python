#filename_sort.py
#https://programmers.co.kr/learn/courses/30/lessons/17686
import sys
sys.stdin=open('input/filename_sort')
from typing import List

def my(filse:List[str])->List[str]:
    answer = []
    convert = []
    for i in files:
        head,number,tail = '','',''
        for idx,j in enumerate(i):
            if not number and j.isdigit():
                head = i[:idx]
            if j.isdigit():
                number+=j
            if number and not j.isdigit():
                tail = i[idx:]
                break
        convert.append([head,number,tail])
    convert.sort(key=lambda x :(x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in convert]
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    files = list(input().split(','))
    answer = my(files)
    print(answer)