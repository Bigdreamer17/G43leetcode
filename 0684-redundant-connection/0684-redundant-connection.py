class Solution:
    def representative(self, x):
        parent = x
        
        while parent != self.rep[parent]:
            parent = self.rep[parent]
            
        while x != self.rep[x]:
            self.rep[x] = parent
            x = self.rep[x]
            
            
        return parent
    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        
        self.rep[xrep] = yrep
        
    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.rep = {i: i for i in range(1, len(edges) + 1)} 
        
        for src, dst in edges:
            if self.connected(src, dst):
                return [src, dst]
            self.union(src, dst)
            
        