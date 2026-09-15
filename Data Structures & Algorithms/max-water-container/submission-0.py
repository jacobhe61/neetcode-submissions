class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        maxArea = 0
        while L < R:
            area = (R - L) * min(heights[R], heights[L])
            if area > maxArea:
                maxArea = area
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxArea