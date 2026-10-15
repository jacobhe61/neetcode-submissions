class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            mask |= 1 << n

        for i in range(len(nums)):
            if not mask & 1:
                return i
            mask >>= 1
        
        return len(nums)
