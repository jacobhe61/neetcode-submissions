class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        vals = sorted(nums)
        for i in range(len(vals)):
            if i == 0 or vals[i] != vals[i-1]:
                L = i+1
                R = len(vals) - 1
                while L < R:
                    if vals[L] + vals[R] + vals[i] == 0:
                        result.append([vals[i], vals[L], vals[R]])
                        L += 1
                        while L < R and vals[L] == vals[L-1]:
                            L += 1
                    elif vals[L] + vals[R] + vals[i] > 0:
                        R -= 1
                        while R > L and vals[R] == vals[R+1]:
                            R -= 1
                    else:
                        L += 1
                        while L < R and vals[L] == vals[L-1]:
                            L += 1
        return result
