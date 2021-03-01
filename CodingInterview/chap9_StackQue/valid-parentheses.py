import sys
sys.stdin = open('input/valid-parentheses')
from typing import List

def my(str:List[str])->bool:
    stack = []

    for i in str:
        if str is '(' or str is '{' or str is '[':
            stack.append(str)

        if str is ')':
            if stack.pop() != '(':
                return False
        elif str is ']':
            if stack.pop()!='[':
                return False
        elif str is '}':
            if stack.pop()!='}':
                return False
    return True

def isValid(s:str)->bool:
    stack=[]
    table = {
        ')':'('
        ,'}':'{'
        ,']':'['
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char]!=stack.pop():
            return False
    return len(stack)==0



strList = list(input().split())
print(my(strList))
print(''.join(strList))