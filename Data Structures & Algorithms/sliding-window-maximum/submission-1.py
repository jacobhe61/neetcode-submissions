class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deque = []
        L = 0
        dqL = 0
        for R in range(len(nums)):
            while deque and nums[R] >= deque[-1][1] and dqL < len(deque):
                deque.pop()
            deque.append([R,nums[R]])
            while R - L + 1 > k:
                L += 1
                if L > deque[dqL][0]:
                    dqL += 1
            if R >= k - 1:
                result.append(deque[dqL][1])
        return result