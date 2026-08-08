class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs = [0] * len(nums)
        lhs[0] = nums[0]
        for i in range(1, len(nums)):
            lhs[i] = lhs[i-1] * nums[i]
        
        rhs = [0] * len(nums)
        rhs[len(nums)-1] = nums[len(nums)-1]
        for i in reversed(range(len(nums)-1)):
            rhs[i] = rhs[i+1] * nums[i]
        
        output = [0] * len(nums)
        for i in range(1, len(nums)-1):
            output[i] = lhs[i-1] * rhs[i+1]
        output[0] = rhs[1]
        output[len(nums)-1] = lhs[len(nums)-2]
        return output
