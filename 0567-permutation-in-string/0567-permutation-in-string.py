class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        Count1 = {}
        
        for i in s1:
            Count1[i] = 1 + Count1.get(i, 0)
            
        l = r = 0
        window = len(s1)
        dis = len(Count1)
        
        while r < len(s2):
            if s2[r] in Count1:
                Count1[s2[r]] -= 1
                if Count1[s2[r]] == 0:
                    dis -= 1
            if r - l + 1 < window:
                r += 1
            else:
                if dis == 0:
                    return True 
                if s2[l] in Count1:
                    Count1[s2[l]] += 1
                    
                    if Count1[s2[l]] == 1:
                        dis += 1
                l += 1
                r += 1
        return False
                
                    