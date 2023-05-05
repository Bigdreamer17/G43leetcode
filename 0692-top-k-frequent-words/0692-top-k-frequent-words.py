class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        Freq = defaultdict(int)
        heap = []
        ans = []
        for word in words:
            Freq[word] -= 1
            
        for item in Freq.items():
            heap.append(item[::-1])
            
        heapify(heap)
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans