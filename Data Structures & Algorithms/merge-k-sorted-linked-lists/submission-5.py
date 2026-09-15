# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode()
        curr = result

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, tuple([lists[i].val, i]))
            lists[i] = lists[i].next if lists[i] else None

        while True:
            if not heap:
                return result.next
            
            pair = heapq.heappop(heap)

            curr.next = ListNode(pair[0])
            curr = curr.next
            
            if lists[pair[1]]:
                heapq.heappush(heap, tuple([lists[pair[1]].val, pair[1]]))
            lists[pair[1]] = lists[pair[1]].next if lists[pair[1]] else None