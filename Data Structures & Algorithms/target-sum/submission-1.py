class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def dfs(i, total):
            if i >= len(nums):
                return total == target
            if tuple([i, total]) in dp:
                return dp[tuple([i, total])]
            
            count = 0
            count += dfs(i+1, total+nums[i])
            count += dfs(i+1, total-nums[i])

            dp[tuple([i, total])] = count
            return count

        return dfs(0, 0)