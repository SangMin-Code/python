# 1991.py
import collections
import sys
from typing import List

sys.stdin = open('input/1991')


def my(n:int,alp:List[str])->List[str]:

    dic = collections.defaultdict(list)
    answer = ["","",""]
    for i in alp:
        temp = i.split()
        dic[temp[0]].append(temp[1])
        dic[temp[0]].append(temp[2])

    def preorder(node):
        if dic[node][0]=='.' and dic[node][1]=='.':
            return node
        left,right="",""
        if dic[node][0].isalpha():
            left = preorder(dic[node][0])
        if dic[node][1].isalpha():
            right = preorder(dic[node][1])
        return node +left + right

    def inorder(node):
        if dic[node][0] == '.' and dic[node][1] == '.':
            return node
        left, right = "", ""
        if dic[node][0].isalpha():
            left = inorder(dic[node][0])
        if dic[node][1].isalpha():
            right = inorder(dic[node][1])
        return left + node + right

    def postorder(node):
        if not dic[node][0].isalpha() and not dic[node][1].isalpha():
            return node
        left, right = "", ""
        if dic[node][0].isalpha():
            left = postorder(dic[node][0])
        if dic[node][1].isalpha():
            right = postorder(dic[node][1])
        return left + right +node

    answer[0]=preorder("A")
    answer[1]=inorder("A")
    answer[2]=postorder("A")

    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    alp = [sys.stdin.readline().rstrip() for _ in range(n)]
    answer = my(n,alp)
    for i in answer:
        print(i)
