class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        curr = 0
        while curr != slow:
            curr = nums[curr]
            slow = nums[slow]
        
        return slow