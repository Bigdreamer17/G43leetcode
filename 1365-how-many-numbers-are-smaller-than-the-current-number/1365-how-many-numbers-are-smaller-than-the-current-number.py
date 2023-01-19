class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        buckets = [0] * 101
        
        for num in nums:
            buckets[num] += 1
        
        prev = 0
        for i, value in enumerate(buckets):
            if value != 0:
                buckets[i] = prev
                prev += value
        return [buckets[num] for num in nums]
        
        """
        O(N ** 2)
        temp = sorted(nums)
        count = 0
        ans = []
        for i in nums:
            for j in temp:
                if i > j:
                    count += 1
            ans.append(count)
            count = 0
        return ans
                """