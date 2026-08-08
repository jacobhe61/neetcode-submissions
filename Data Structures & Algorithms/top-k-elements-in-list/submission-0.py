class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        frequencies = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            frequencies[value].append(key)
        
        result = []
        for i in reversed(frequencies):
            for j in i:
                if len(result) != k:
                    result.append(j)
        
        return result