# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        left_prev, curr = dummy, head
        # skip to left
        for _ in range(1, left):
            left_prev = curr
            curr = curr.next

        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy.next 