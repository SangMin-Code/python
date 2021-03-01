#add-two-numbers
import functools
from typing import List
from operator import add,mul

class ListNode(object):
    def __init__(self,x):
            self.val=x
            self.next = None

a = ListNode(2)
a.next=ListNode(4)
a.next.next=ListNode(3)

b=ListNode(5)
b.next=ListNode(6)
b.next.next=ListNode(4)

def myreverse(head:ListNode)->ListNode:
    node, prev = head,None
    while node :
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

def mytoNum(head:ListNode)->int:
    node = head
    numList = []
    while node:
        numList.append(node.val)
        node = node.next
    return int(''.join(str(e) for e in numList))

def mysumNode(a:ListNode, b:ListNode)->ListNode:
    a_reverse = myreverse(a)
    b_reverse = myreverse(b)
    a_num =mytoNum(a_reverse)
    b_num=mytoNum(b_reverse)
    sum_num = a_num+b_num
    sum_str = str(sum_num)
    head = ListNode(sum_str[0])
    c= head
    for i in range(1,len(sum_str)):
        c.next = ListNode(sum_str[i])
        c=c.next
    head =myreverse(head)
    return head

def reverseList(head:ListNode)->ListNode:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

def toList(node:ListNode)->ListNode:
    list:List=[]
    while node:
        list.append(node.val)
        node = node.next
    return list

def toReversedLinkedList(result:ListNode)->ListNode:
    prev:ListNode =None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
    return node

def addTwoNumbers(l1:ListNode, l2:ListNode)->ListNode:
    a= toList(reverseList(l1))
    b=toList(reverseList(l2))
    resultStr = int(''.join(str(e) for e in a))+\
                int(''.join(str(e) for e in b))
    return toReversedLinkedList(str(resultStr))

def adder(l1:ListNode, l2:ListNode)->ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum+=l1.val
            l1 = l1.next
        if l2 :
            sum +=l2.val
            l2 = l2.next
        carry,val = divmod(sum+carry,10)
        head.next = ListNode(val)
        head = head.next
    return root.next

answer1 =mysumNode(a,b)
answer2= addTwoNumbers(a,b)

#숫자형 리스트를 단일 값으로 병합하기

test = [1,2,3,4,5]
''.join(str(e) for e in test)
''.join(map(str,a))
functools.reduce(lambda x,y :10*x+y,test,0)
functools.reduce(add,test)
functools.reduce(mul,test)
