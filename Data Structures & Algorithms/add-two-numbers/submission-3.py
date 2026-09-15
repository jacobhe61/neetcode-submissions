# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        result = ListNode()
        curr3 = result
        carry = 0
        while curr1 or curr2 or carry:
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0
            sum = num1 + num2 + carry
            val = sum % 10
            carry = sum // 10

            curr3.next = ListNode(val, None)
            curr3 = curr3.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return result.next