#ReorderLogFiles
import sys
from typing import List

sys.stdin = open('input/ReorderLogFiles','r')


def my():
    n = int(input())
    letlogs=[]
    diglogs=[]
    for i in range(n):
        s= input()
        if 'dig' in s.split()[0]:
           diglogs.append(s)
        else :
            letlogs.append(s)
    #letlogs.sort(key=lambda x : (x.split()[1:],x.split()[0])) #sort
    for i in range(len(letlogs)):
        for j in range(1,len(letlogs)):
            if compare(letlogs[i],letlogs[j]):
                letlogs[i],letlogs[j]=letlogs[j],letlogs[i]
    print(letlogs+diglogs)

def compare(s1:List[str], s2:List[str])->bool:
    n = len(s1)-1
    for i in range(1,n):
        if s1[i]>s2[i]:
            return True
        elif s1[i]<s2[i]:
            return False

def reorderFiles(logs:List[str])->List[str]:
    letters,digits = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else :
            letters.append(log)
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
    return letters+digits

my()
'''
n=int(input())
logs=[]
for i in range(n):
    logs.append(input())
print(reorderFiles(logs))
'''


'''
람다표현식
식볋자 없이 실행 가능한 함수
'''