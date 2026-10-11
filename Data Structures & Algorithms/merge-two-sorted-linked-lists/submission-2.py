# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # add list2 nodes on to list1
        dummy = ListNode(next=list1)
        prev = dummy
        while list1 and list2:
            if list1.val < list2.val:
                prev = list1
                list1 = list1.next
            else:
                temp = list2.next
                prev.next = list2
                prev = list2
                list2.next = list1
                list2 = temp
        
        if list2:
            prev.next = list2
        return dummy.next