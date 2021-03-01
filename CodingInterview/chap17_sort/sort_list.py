from CodingInterview.my_util.Util import ListNode
import sys
sys.stdin = open('input/sort_list')


def mergeTwoLists(l1:ListNode, l2:ListNode)->ListNode:
    if l1 and l2:
        if l1.value > l2.value:
            l1,l2 = l2,l1
        l1.next = mergeTwoLists(l1.next,l2)
    return l1 or l2

def sortList(head:ListNode)->ListNode:
    if not (head and head.next):
        return head
    half,slow, fast = None,head,head
    while fast and fast.next:
        half ,slow, fast = slow, slow.next, fast.next.next
    half.next = None
    l1 = sortList(head)
    l2 = sortList(slow)
    return mergeTwoLists(l1, l2)

def built_in_function(head:ListNode)->ListNode:
    p = head
    lst =[]
    while p:
        lst.append(p.value)
        p=p.next
    lst.sort()

    p=head
    for i in range(len(lst)):
        p.value = lst[i]
        p=p.next
    return head



TC = int(input())
for test_case in range(1,TC+1):
    nums = list(map(int,input()))
    head =  ListNode(None)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    root = head.next




