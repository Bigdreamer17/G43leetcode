class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-float('inf'))
        monostack = [(0, -1)]
        area = 0
        for indx in range(1, len(heights)):
            cur_lb = indx - 1
            while monostack and heights[monostack[-1][0]] > heights[indx]:
                i,left_bound = monostack.pop()
                cur_lb = left_bound
                area =  max(area, (indx - left_bound - 1) * heights[i])
                
            monostack.append((indx, cur_lb))
        return area