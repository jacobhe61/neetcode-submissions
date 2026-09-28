class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0
        for n in nums:
            sum = max(0, sum) + n
            res = max(res, sum)
        
        return res
            