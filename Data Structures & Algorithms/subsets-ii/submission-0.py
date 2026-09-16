class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def recur(i, arr):
            nonlocal res

            if i == len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            recur(i+1, arr)
            arr.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            recur(i+1, arr)

        recur(0, [])    
        return res