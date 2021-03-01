#swap-node-pairs

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def my(head:ListNode)->ListNode:
    node = head
    while node and node.next:
        node.val, node.next.val = node.next.val,node.val
        node = node.next.next
    return head



def swapPairs(head:ListNode)->ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        #b가 a(head)를 가리키도록 할당
        b=head.next
        head.next=b.next
        b.next =head
        #prev가 b를 가리키도록 할당
        prev.next=b
        #다음번 비교를 위해 이동
        head = head.next
        prev=prev.next.next

    return root.next

def reculsion(head:ListNode)->ListNode:
    if head and head.next:
        p = head.next
        #스왑된 값 리턴 받음
        head.next = reculsion(p.next)
        p.next=head
        return p
    return head



head=ListNode(None)
node=head
for i in range(1,4+1):
    node.next = ListNode(i)
    node= node.next
#my(head)

answer =swapPairs(head.next)
while answer:
    print(answer.val)
    answer = answer.next

