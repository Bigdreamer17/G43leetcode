class Solution:
    # def __init__(self):
    #     self.rep = defaultdict(str)
    
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
        
        self.rep[xrep] = self.rep[yrep]
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if not edges:
            return source == destination
        self.rep = {i: i for i in range(n)} 
        
        for src, des in edges:
            self.union(src, des)
            
        return self.representative(source) == self.representative(destination)