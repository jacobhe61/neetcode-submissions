class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * 2

        for i in range(len(cost)-1, -1, -1):
            temp = arr[1]
            arr[1] = cost[i] + min(arr)
            arr[0] = temp
        
        return min(arr)