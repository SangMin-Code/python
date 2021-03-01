import sys
from typing import List,Deque
import collections
sys.stdin=open('input/palindrome-linked-list')

class ListNode(object):
    def __init__(self,x):
            self.val=x
            self.next = None

def to_list(head:ListNode) ->bool:
    q:List = []
    if not head:
        return True
    node =head
    #리스트 변환
    while node is not None:
        q.append(node.val)
        node=node.next
    #팰린드롬 판별
    while len(q)>1:
        if q.pop(0)!=q.pop():
            return False
    return True

def to_deque(head:ListNode)->bool:
    #데크 자료형 선언
    q:Deque = collections.deque()

    if not head :
        return True
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q)>1:
        if q.popleft() != q.pop():
            return False
    return True

def runner(head:ListNode)->bool:
    rev = None
    slow = fast = head
    #런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    #리스트 홀,짝의 경우 나눔
    if fast:
        slow = slow.next

    #팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow,rev = slow.next,rev.next
    return not rev

TC = int(input())
for test_case in range(1,TC+1):
    xList = list(map(int,input().split()))
    head = ListNode(xList[0])
    p = head
    for i in range(1,len(xList)):
        p.next = ListNode(xList[i])
        p=p.next
    print(to_list(head))




