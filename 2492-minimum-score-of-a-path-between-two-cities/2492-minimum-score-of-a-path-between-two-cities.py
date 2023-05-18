class Union:
    def  __init__(self, n):
        self.rep = {i:i for i in range(1, n +1)}
        self.size = {i:1 for i in range(1, n +1)}
        # self.min = {i:iinf for i in range(n)}
        
    def find(self,x):
        if self.rep[x] == x :
            return x
        parent = self.find(self.rep[x])
        self.rep[x] = parent
        return self.rep[x]
    
    def union(self, x ,y):
        Xrep = self.find(x)
        Yrep = self.find(y)
        
        if Xrep != Yrep:
            if self.size[Xrep] > self.size[Yrep]:
                self.rep[Yrep] = Xrep
            elif self.size[Xrep]  < self.size[Yrep]:
                self.rep[Xrep] = Yrep
            else:
                self.rep[Xrep] = Yrep
                self.size[Yrep] += 1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minDistance = float(inf)
        uf = Union(n)
        
        for src, dst, dist in roads:
            uf.union(src , dst)
        
        for src, dst, dist in roads:
            if uf.connected(src, 1):
                minDistance = min(minDistance, dist)
                
        return minDistance