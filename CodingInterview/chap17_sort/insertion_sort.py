from CodingInterview.my_util.Util import ListNode

def insertion_sort_list(head:ListNode)->ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.value <head.value:
            cur = cur.next
        cur.next, head.next, head = head, cur.next,head.next
        if head and cur.val>head.val:
            cur = parent
    return cur.next