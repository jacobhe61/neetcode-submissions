class Solution:
    def find(self, node, par):
        while node != par[node]:
            par[node] = par[par[node]]
            node = par[node]
        return node

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for i in range(1, len(edges)+1):
            par[i] = i
            rank[i] = 0
        
        for src, dst in edges:
            p1 = self.find(src, par)
            p2 = self.find(dst, par)

            if p1 == p2:
                return [src, dst]

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
        
        return edges[-1]