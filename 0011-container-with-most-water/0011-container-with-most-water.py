class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
       
        while left < right:
            width = right - left
            length = min(height[left], height[right])
            area = width * length 
            ans = max(ans, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans