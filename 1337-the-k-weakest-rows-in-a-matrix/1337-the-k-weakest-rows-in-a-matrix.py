class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        ones_count = []     
        for i in range(len(mat)):
            ones_count.append((mat[i].count(1) , i))
        heapify(ones_count)
        
        for _ in range(k):
            heap.append(heappop(ones_count)[1])
            
        return heap