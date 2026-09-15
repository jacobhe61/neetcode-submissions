class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            M = (L+R)//2
            
            if nums[M] < nums[L]:
                if target < nums[M]:
                    R = M - 1
                elif target > nums[M]:
                    if target > nums[L]:
                        R = M - 1
                    elif target < nums[L]:
                        L = M + 1
                    else:
                        return L
                else:
                    return M
            elif nums[M] > nums[R]:
                if target > nums[M]:
                    L = M + 1
                elif target < nums[M]:
                    if target < nums[R]:
                        L = M + 1
                    elif target > nums[R]:
                        R = M - 1
                    else:
                        return R
                else:
                    return M
            else:
                if target < nums[M]:
                    R = M - 1
                elif target > nums[M]:
                    L = M + 1
                else:
                    return M
        return -1
