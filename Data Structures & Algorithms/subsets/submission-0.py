class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(i, arr):
            nonlocal res

            if i >= len(nums):
                res.append(arr[:])
                return
            
            arr.append(nums[i])
            recur(i + 1, arr)
            arr.pop()
            recur(i + 1, arr)

        recur(0, [])
        return res