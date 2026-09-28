class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pt = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= pt:
                pt = i

        return pt == 0