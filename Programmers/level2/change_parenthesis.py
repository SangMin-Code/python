#change_parenthesis.py
#https://programmers.co.kr/learn/courses/30/lessons/60058
import sys

sys.stdin=open('input/change_parenthesis')
from typing import List

def my(perenthesis:str)->str:
    dic = {"(":")", ")":"(" }
    def is_correct(s):
        correct =True
        stack = []
        for i,p in enumerate(s):
            if not stack:
                stack.append(p)
                if p !='(':
                    return False
            else :
                if dic[stack[-1]]==p:
                    stack.pop()
                else :
                    stack.append(p)
        return True

    def recursion(s):
        if len(s) == 0 or is_correct(s):
            return s
        idx = len(s)-1
        stack =[]
        for i,p in enumerate(s):
            if stack:
                if dic[stack[-1]] == p:
                    stack.pop()
                    if not stack:
                        idx = i
                        break
                    continue
            stack.append(p)
        u = s[:idx+1]
        v = s[idx+1:]
        if is_correct(u):
            return  u + recursion(v)
        else :
            answer = '('+recursion(v)+')'
            for c in u[1:-1]:
                answer +=dic[c]
        return answer
    return recursion(parenthesis)





TC = int(input())
for test_case in range(1,TC+1):
    parenthesis = input()
    answer =my(parenthesis)
    print(answer)