class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l = r = 0
        answer = []
        
        while l < len(firstList) and  r < len(secondList):
            l_start, l_end = firstList[l]
            r_start, r_end = secondList[r]
            
            if l_start <= r_end and r_start <= l_end:
                answer.append([max(l_start, r_start), min(l_end, r_end)])
            
            if l_end <= r_end:
                l += 1
            else:
                r += 1
        return answer
            
            