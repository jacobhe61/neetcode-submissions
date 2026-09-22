class Solution:
    def find(self, node, par):
        while par[node] != node:
            par[node] = par[par[node]]
            node = par[node]
        return node

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = {}
        rank = {}
        
        for i in range(n):
            par[i] = i
            rank[i] = 0

        for src, dst in edges:
            p1 = self.find(src, par)
            p2 = self.find(dst, par)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
        
        return len(edges) == n-1