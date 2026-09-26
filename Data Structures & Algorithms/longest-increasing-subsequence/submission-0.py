import math

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            high = 0
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    high = max(high, dp[j])
            dp[i] = high+1
        
        return max(dp)
        