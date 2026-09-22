class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        valid = set()

        def dfs(i):
            if not adj[i] or i in valid:
                return True
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            valid.add(i)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True