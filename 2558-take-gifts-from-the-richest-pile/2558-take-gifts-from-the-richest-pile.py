class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = gifts[i] * -1
        heapify(gifts)
        
        while k != 0:
            max_number = sqrt(-1 * heappop(gifts))
            heappush(gifts, max_number)
            
            for i in range(len(gifts)):
                if gifts[i] > 0:
                    gifts[i] = int(gifts[i] * -1)
            k -= 1
           
        return -(sum(gifts))
        