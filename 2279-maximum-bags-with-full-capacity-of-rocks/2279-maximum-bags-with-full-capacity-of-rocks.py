class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = 0
        remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]
        remaining_capacity.sort()
        
        for i in remaining_capacity:
            if additionalRocks >= i:
                additionalRocks -= i
                bags += 1
            else:
                break
         
        return bags