# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        curr = l1
        i = 0
        while curr:
            num1 += curr.val * (10 ** i)
            curr = curr.next
            i += 1

        num2 = 0
        curr = l2
        i = 0
        while curr:
            num2 += curr.val * (10 ** i)
            curr = curr.next
            i += 1
        
        sum = num1 + num2
        if sum == 0:
            return ListNode(0, None)

        i = 0
        result = ListNode()
        top = result
        while sum != 0:
            top.next = ListNode(sum % 10, None)
            top = top.next
            sum = sum // 10
        
        return result.next