class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        dp = [1, 1]

        for i in range(len(nums)):
            if not nums[i]:
                dp = [1, 1]

            mini = dp[0]
            maxi = dp[1]

            dp[0] = min(maxi * nums[i], mini * nums[i], nums[i])
            dp[1] = max(maxi * nums[i], mini * nums[i], nums[i])

            res = max(res, dp[1])

        return res
