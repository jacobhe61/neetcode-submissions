class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        
        def dfs(i, robbed):
            if i >= len(nums):
                return 0
            if robbed and i == len(nums)-1:
                return 0
            if tuple([i, robbed]) in dp:
                return dp[tuple([i, robbed])]
            
            if not i:
                dp[tuple([i, robbed])] = max(dfs(i+1, False), nums[i] + dfs(i+2, True))
            else:
                dp[tuple([i, robbed])] = max(dfs(i+1, robbed), nums[i] + dfs(i+2, robbed))
            
            return dp[tuple([i, robbed])]
        
        return dfs(0, False)