# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev2 = None
        prev1 = None
        while (curr and curr.next != None):
            prev2 = prev1
            prev1 = curr
            curr = curr.next
            prev1.next = prev2
        if curr:
            curr.next = prev1

        return curr
        
        
