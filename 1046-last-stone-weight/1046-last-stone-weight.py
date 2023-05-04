class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            sorted_stones = sorted(stones)
            
            stone1 , stone2 = sorted_stones[-1], sorted_stones[-2]
            
            if stone1 == stone2:
                stones = sorted_stones[:-2]
            else:
                sorted_stones.remove(stone2)
                sorted_stones.remove(stone1)
                sorted_stones.append(stone1 -stone2)
                stones = sorted_stones
                
        if len(stones) == 1:
            return stones[0]
        else:
            return 0