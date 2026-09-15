# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = head
        mid = head
        back = head
        for i in range(k-1):
            mid = mid.next if mid else None
        if mid:
            head = mid
        for i in range(2*k-1):
            front = front.next if front else None
        while True:
            if mid and front:
                prev = front
            elif mid:
                prev = mid.next
            else:
                return head
            for i in range(k):
                temp = back.next
                back.next = prev
                prev = back
                back = temp

                mid = mid.next if mid else None
                front = front.next if front else None