class Solution:
    def find(self, node, par):
        while par[node] != node:
            par[node] = par[par[node]]
            node = par[node]
        return node
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}
        
        for i in range(n):
            par[i] = i
            rank[i] = 0
        
        count = 0
        for src, dst in edges:
            p1 = self.find(src, par)
            p2 = self.find(dst, par)

            if p1 == p2:
                continue
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            
            count += 1
                
        return n - count
