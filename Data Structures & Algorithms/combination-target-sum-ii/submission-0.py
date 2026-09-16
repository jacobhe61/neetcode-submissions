class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def recur(i, arr, sum):
            nonlocal res

            if sum == target:
                res.append(arr.copy())
                return

            if sum > target:
                return

            prev = 0
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                arr.append(candidates[j])
                recur(j+1, arr, sum + candidates[j])
                arr.pop()
                prev = candidates[j]
            
        recur(0, [], 0)
        return res