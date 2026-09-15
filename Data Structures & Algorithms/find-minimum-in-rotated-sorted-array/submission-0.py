class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        small = nums[0]

        while L <= R:
            M = (L+R)//2

            if nums[M] < nums[L]:
                R = M - 1
                small = min(small, nums[M])
            elif nums[M] > nums[R]:
                L = M + 1
                small = min(small, nums[M])
            else:
                small = min(small, nums[L])
                return small
