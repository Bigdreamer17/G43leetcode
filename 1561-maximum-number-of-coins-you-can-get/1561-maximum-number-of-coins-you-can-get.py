class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[len(piles) // 3: ]
        me = 0
        i = 0
        
        while i < len(piles):
            me += piles[i]
            i += 2
        
        return me 