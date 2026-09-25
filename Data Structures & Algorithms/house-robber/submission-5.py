class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * 3

        for i in range(len(nums)-1, -1, -1):
            temp1 = dp[2]
            temp2 = dp[1]
            dp[2] = max(dp[0], dp[1]) + nums[i]
            dp[1] = temp1
            dp[0] = temp2

        return max(dp[2], dp[1])