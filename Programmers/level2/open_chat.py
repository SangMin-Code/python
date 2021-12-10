#open_chat.py
#https://programmers.co.kr/learn/courses/30/lessons/42888
import sys
sys.stdin=open('input/open_chat')
from typing import List
import collections

def my(chat:List[str])->List[str]:
    answer = []*len(chat)
    userId_dic = collections.defaultdict(str)
    converse_dic = {"Enter":"들어왔습니다.", "Leave":"나갔습니다"}

    for c in chat:
        strs = c.split()
        if strs[0] !="Leave":
            userId_dic[strs[1]]=strs[2]

    for c in chat:
        strs = c.split()
        if strs[0] != "Change":
            answer.append(userId_dic[strs[1]]+"님이 "+converse_dic[strs[0]])

    return answer



TC = int(input())
for test_case in range(1,TC+1):
    chat = []
    n = int(input())
    for _ in range(n):
        chat.append(input())
    answer =my(chat)
    print(answer)