#merge-two-sorted-lists
import sys
sys.stdin=open('input/merge-two-sorted-lists')


class ListNode(object):
    def __init__(self,x):
            self.val=x
            self.next = None

def my(a:ListNode, b:ListNode) ->ListNode:
    c = ListNode(None)
    head = c
    while a and b :
        if a.val >= b.val:
            head.next = ListNode(b.val)
            head = head.next
            b=b.next
        else :
            head.next = ListNode(a.val)
            head = head.next
            a=a.next
    if a :
        head.next = a
    if b :
        head.next = b
    while c :
        print(c.val)
        c= c.next

def reculsion(l1:ListNode, l2:ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1
    if l1 :
        l1.next = reculsion(l1.next,l2)
    return l1


a= ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(4)

b=ListNode(1)
b.next=ListNode(3)
b.next.next=ListNode(4)


my(a,b)











