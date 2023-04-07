class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set()
        destinations = set()
        origins = set()
        for o, d in edges:
            destinations.add(d)
            origins.add(o)
        for edge in edges:
            if edge[0] in origins and edge[0] not in destinations:
                ans.add(edge[0])
        return ans