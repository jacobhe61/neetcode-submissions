class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxheight = 0
        for i in heights:
            if i > maxheight:
                maxheight = i

        maxarea = 0
        arr = [0] * maxheight
        for i in heights:
            for j in range(i):
                arr[j] += 1
                area = arr[j] * (j+1)
                if area > maxarea:
                    maxarea = area
            for j in range(i, maxheight):
                arr[j] = 0
        
        return maxarea
        
