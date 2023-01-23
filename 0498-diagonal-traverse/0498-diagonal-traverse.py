class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        
        rows = len(mat)
        cols = len(mat[0])
        
        for r in range(rows):
            for c in range(cols):
                hashmap[r+c].append(mat[r][c])
        
        ans = []
        for k,v in hashmap.items():
            if k%2==0:
                ans += v[::-1]
            else:
                ans += v
        
        return ans