class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        
        for index, value in enumerate(nums):
            if value in seen and index - seen[value] <= k:
                return True
            else:
                seen[value] = index
        return False