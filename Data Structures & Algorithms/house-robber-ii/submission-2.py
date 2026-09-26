class Solution:
    def helper(self, dp, nums, start, end):
        for i in range(start, end, -1):
            temp = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = temp

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [0, 0]
        dp2 = [0, 0]

        self.helper(dp1, nums, len(nums)-1, 0)
        self.helper(dp2, nums, len(nums)-2, -1)

        return max(dp1[1], dp2[1])
