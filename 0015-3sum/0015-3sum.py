class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hmap = dict()
        for i in range(n):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        
        ans = set()
        for i in range(n-2):
			
            hmap[nums[i]] -= 1
            for j in range(i+1, n-1):
				
                hmap[nums[j]] -= 1
                rem = -(nums[i]+nums[j])
                if rem in hmap and hmap[rem] > 0:
                    ans.add(tuple(sorted((nums[i], nums[j], rem))))
                hmap[nums[j]] += 1
            hmap[nums[i]] += 1
        
        res = []
        for i in ans:
            res.append(list(i))
        return res