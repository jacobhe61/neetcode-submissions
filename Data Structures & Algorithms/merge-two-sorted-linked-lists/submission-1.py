# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1):
            return list2
        elif (not list2):
            return list1
        curr1 = list1
        curr2 = list2
        list3 = ListNode()
        top = list3
        while (curr1 and curr2):
            if (curr2.val <= curr1.val):
                top.next = curr2
                top = curr2
                curr2 = curr2.next
            elif (curr1.val < curr2.val):
                top.next = curr1
                top = curr1
                curr1 = curr1.next
        top.next = curr1 if curr1 else curr2
        return list3.next