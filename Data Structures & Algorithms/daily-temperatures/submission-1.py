class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        colder = []
        indices = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(colder) != 0 and temperatures[i] > colder[-1]:
                result[indices[-1]] = i-indices[-1]
                colder.pop()
                indices.pop()
            colder.append(temperatures[i])
            indices.append(i)
        for i in indices:
            result[i] = 0
        return result
