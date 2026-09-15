# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        for i in range((length+1)//2):
            prev = curr
            curr = curr.next
        prev.next = None

        prev = None
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        currFront = head
        currBack = prev
        result = ListNode()
        top = result
        while (currFront and currBack):
            top.next = currFront
            top = currFront
            currFront = currFront.next
            top.next = currBack
            top = currBack
            currBack = currBack.next 
        top.next = currFront

        head = result.next