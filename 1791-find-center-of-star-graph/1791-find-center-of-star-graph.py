class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertex = set()
        for e in edges:
            if e[0] in vertex:
                return e[0]
            if e[1] in vertex:
                return e[1]
            
            vertex.add(e[0])
            vertex.add(e[1])
        