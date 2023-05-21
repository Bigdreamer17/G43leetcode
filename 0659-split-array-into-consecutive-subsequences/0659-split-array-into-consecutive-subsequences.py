class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ends_with = defaultdict(list)
        for n in nums:
            if ends_with[n-1]:
                length = heapq.heappop(ends_with[n-1])
                heapq.heappush(ends_with[n], length+1)
            else:
                heapq.heappush(ends_with[n], 1)

        for lengths in ends_with.values():
            if lengths and lengths[0] < 3:
                return False
        
        return True