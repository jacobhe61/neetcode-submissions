from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()
        L = 0
        for R in range(len(nums)):
            while dq and nums[R] >= dq[-1][1]:
                dq.pop()
            dq.append([R,nums[R]])
            while R - L + 1 > k:
                L += 1
                if L > dq[0][0]:
                    dq.popleft()
            if R >= k - 1:
                result.append(dq[0][1])
        return result