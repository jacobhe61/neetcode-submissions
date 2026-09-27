class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = defaultdict(int)
        prev[0] += 1

        for i in range(len(nums)):
            curr = defaultdict(int)
            for j, k in prev.items():
                curr[j + nums[i]] += k
                curr[j - nums[i]] += k
            prev = curr
        
        return prev[target]

        