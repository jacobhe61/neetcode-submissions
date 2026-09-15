# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head):
            return False
        curr1 = head
        curr2 = head.next
        while (curr1 and curr2):
            curr1 = curr1.next
            curr2 = curr2.next
            if (not curr2):
                return False
            if curr2 == curr1:
                return True
            curr2 = curr2.next
            if curr2 == curr1:
                return True
        return False