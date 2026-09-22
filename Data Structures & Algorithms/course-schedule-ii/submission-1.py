class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for src, dst in prerequisites:
            adj[src].append(dst)

        valid = set()
        visited = set()
        def dfs(i):
            if i in valid:
                return True
            if not adj[i]:
                valid.add(i)
                res.append(i)
                return True
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            
            valid.add(i)
            res.append(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res