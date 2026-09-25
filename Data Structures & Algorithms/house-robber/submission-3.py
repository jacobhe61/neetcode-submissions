class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums) or i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            robbed = dfs(i+2)
            if i+3 < len(nums):
                robbed = max(robbed, dfs(i+3))
            
            dp[i] = nums[i] + robbed

            return dp[i]
        
        return max(dfs(0), dfs(1))