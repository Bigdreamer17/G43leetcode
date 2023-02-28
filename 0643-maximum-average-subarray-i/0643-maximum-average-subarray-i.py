class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_subarray = sum(nums[:k])
        ave = cur_subarray / k
        
        for i in range(1, len(nums)-k+1):
            cur_subarray = cur_subarray - nums[i-1]
            cur_subarray = cur_subarray + nums[i+k-1]
            
            ave2 = cur_subarray / k
            ave = max(ave, ave2)
        return ave
        