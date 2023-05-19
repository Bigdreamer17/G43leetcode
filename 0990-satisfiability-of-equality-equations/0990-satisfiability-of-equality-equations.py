class UnionFind:
    def __init__(self,n):
        self.rep = {chr(97 + i):chr(97 + i) for i in range(27)}
        
    def find(self,x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        
        return self.rep[x]
    
    def union(self, x, y):
        Repx = self.find(x)
        Repy = self.find(y)
        
        if Repx != Repy:
            self.rep[Repy] = Repx
    
    def isconnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(len(equations))
        
        for i in range(len(equations)):
            if equations[i][1] == '=':
                uf.union(equations[i][0], equations[i][3])
        for i in range(len(equations)):
            if equations[i][1] == '!' and uf.isconnected(equations[i][0], equations[i][3]):
                return False
           
        return True