class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recur(i, arr, sum):
            nonlocal res

            if sum == target:
                res.append(arr.copy())
                return
            if sum > target:
                return

            for j in range(i, len(nums)):
                arr.append(nums[j])
                recur(j, arr, sum + nums[j])
                arr.pop()

        recur(0, [], 0)
        return res