import sys

class ListNode(object):
    def __init__(self,x):
            self.val=x
            self.next = None

def my(node:ListNode)->ListNode:
    nodeList = []
    while node :
        nodeList.append(node.val)
        node=node.next
    head = ListNode(nodeList.pop())
    b=head
    while nodeList:
        b.next = ListNode(nodeList.pop())
        b=b.next
    c=head
    while c:
        print(c.val)
        c=c.next
    return head

def reculsive(head:ListNode)->ListNode:
    def reverse(node:ListNode, prev:ListNode=None):
        if not node:
            return prev
        next,node.next = node.next,prev
        return reverse(next,node)
    return reverse(head)

def iterative(head:ListNode)->ListNode:
    node,prev = head,None

    while node:
        next,node.next = node.next, prev
        prev,node = node, next
    return prev


a = ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)

my(a)