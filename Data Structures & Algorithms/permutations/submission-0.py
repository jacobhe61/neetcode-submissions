class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(i):
            if i >= len(nums):
                return [[]]
            
            res = []
            for l in recur(i+1):
                for j in range(len(l)+1):
                    l.insert(j, nums[i])
                    res.append(l.copy())
                    l.pop(j)
            return res
        
        return recur(0)