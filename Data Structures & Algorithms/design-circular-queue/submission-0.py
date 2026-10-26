class ListNode:
    def __init__(self, val, nxt = None):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.left = ListNode(0)
        self.right = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        cur = ListNode(value)
        if self.isEmpty():
            self.left.next = cur
            self.right = cur
        else:
            self.right.next = cur
            self.right = cur
        self.length -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        if self.left.next is None:
            self.right = self.left
        self.length += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.val

    def isEmpty(self) -> bool:
        return self.left.next is None

    def isFull(self) -> bool:
        return self.length == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()