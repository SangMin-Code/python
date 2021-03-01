class ListNode:
    def __init__(self,x):
        self.value = None
        self.next = None

class CircularDeque:
    def __init__(self, k:int):
        self.head, self.tail = ListNode(None),ListNode(None)
        self.k,self.len = k,0
        self.head.right,self.tail.left=self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):  # 내부함수에는 _ 를 붙임
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self,node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value:int)->bool:
        if self.len == self.k:
            return False
        else:
            self.len+=1
            self._add(self.head,ListNode(value))
            return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self._add(self.tail.left, ListNode(value))
            return True

    def deleteFront(self)->bool:
        if self.len==0:
            return False
        self.len -=1
        self._del(self.head)
        return True

    def deleteLast(self)->bool:
        if self.len==0:
            return False
        self.len -=1
        self._del(self.tail.left.left)
        return True
    def getFront(self)->int:
        return self.head.right.value if self.len else -1
    def getRear(self)->int:
        return self.tail.left.value if self.len else -1
    def isEmpty(self)->bool:
        return self.len==0
    def isFull(self)->bool:
        return self.len==self.k

    

