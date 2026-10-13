# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None
        # recursive case
        # record newHead
        newHead = head
        # if there is still a subproblem
        if head.next:
            # solve subproblem first
            newHead = self.reverseList(head.next)
            # reverses link between next node and head
            head.next.next = head
        # set end.next to nothing
        head.next = None
        # basically previous
        return newHead