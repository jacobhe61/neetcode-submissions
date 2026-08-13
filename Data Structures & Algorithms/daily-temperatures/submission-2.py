class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(indices) != 0 and temperatures[i] > temperatures[indices[-1]]:
                result[indices[-1]] = i-indices[-1]
                indices.pop()
            indices.append(i)
        for i in indices:
            result[i] = 0
        return result
