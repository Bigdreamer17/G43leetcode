class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}
        
        def find(x):
            rep.setdefault(x,x)
            if x != rep[x]:
                rep[x] = find(rep[x])
            return rep[x]
        def union(x, y):
            rootX = find(x)
            rootY= find(y)

            if rootX > rootY:
                rep[rootX] = rootY
            else:
                rep[rootY] = rootX
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        ans = []
        
        for ch in baseStr:
            ans.append(find(ch))
            
        return ''.join(ans)
        