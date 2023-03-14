class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        queue = deque()
        ans = []
        for r, val in enumerate(nums):
            while queue and nums[queue[-1]] <  val:
                queue.pop()
            queue.append(r)
            
            if r >=  k - 1:
                if queue[0] >= r +  1 - k:
                    ans.append(nums[queue[0]])
                else:
                    while queue[0] < r +  1 - k:
                        queue.popleft()
                    ans.append(nums[queue[0]])
        return ans
                