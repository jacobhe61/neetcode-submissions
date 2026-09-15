class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        unresolved = []
        heights.append(0)
        for i in range(len(heights)):
            leftIndex = i
            height = heights[i]
            while len(unresolved) > 0 and height < unresolved[-1][1]:
                top = unresolved.pop()
                leftIndex = top[0]
                area = (i - leftIndex) * top[1]
                if area > maxArea:
                    maxArea = area
            unresolved.append([leftIndex, height])
        return maxArea