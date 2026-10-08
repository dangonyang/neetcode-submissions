# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # input: two linked lists
        # output: one linked list
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        second_head = l2
        
        # dummy node because head might change
        # iterate through both linked lists
        #   sum l1 and l2 value
        #   sum % 10 for current value
        #   sum // 10 carry over to next value
        #   update current l2 value to mod + carry
        # check if there's an extra carry, then add new node
        # return head

        dummy = ListNode(next=head)
        prev = dummy
        carry = 0
        while head or second_head:
            if not head:
                head = ListNode(0)
                prev.next = head
            elif not second_head:
                second_head = ListNode(0)
            node_sum = head.val + second_head.val + carry
            carry = node_sum // 10
            head.val = node_sum % 10

            prev = head
            head = head.next
            second_head = second_head.next
        if carry != 0:
            prev.next = ListNode(carry, None)
        return dummy.next

