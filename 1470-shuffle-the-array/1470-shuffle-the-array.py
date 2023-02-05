class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        first = nums[0:half]
        sec = nums[half:]
        ans = []
        f = 0
        s = 0
        while f < len(first):
            ans.append(first[f])
            ans.append(sec[s])
            f += 1
            s += 1
        return ans