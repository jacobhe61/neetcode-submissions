class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        vals = sorted(nums)
        for n in nums:
            i = vals.index(n)
            vals.pop(i)
            L = 0
            R = len(vals) - 1
            while L < R:
                if vals[L] + vals[R] + n == 0:
                    elem = tuple(sorted([n, vals[L], vals[R]]))
                    if elem not in seen:
                        result.append([n, vals[L], vals[R]])
                        seen.add(elem)
                    L += 1
                elif vals[L] + vals[R] + n > 0:
                    R -= 1
                else:
                    L += 1
            vals.insert(i, n)
        return result
