class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i+1 >= len(nums) or i+2 >= len(nums):
                return nums[i]
            if i in dp:
                return dp[i]

            robbed = dfs(i+2)
            if i+3 < len(nums):
                robbed = max(robbed, dfs(i+3))
            
            dp[i] = nums[i] + robbed

            return dp[i]
        
        if len(nums) == 1:
            return nums[0]

        return max(dfs(0), dfs(1))