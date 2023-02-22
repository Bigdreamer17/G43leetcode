class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = {}
        
        for i in p:
            countP[i] = 1 + countP.get(i, 0)
        
        l = r = 0
        dis = len(countP)
        window = len(p)
        ans = []
        
        while r < len(s):
            if s[r] in countP:
                countP[s[r]] -= 1
                
                if countP[s[r]] == 0:
                    dis -= 1
            if (r - l + 1 < window):
                r += 1
            else:
                if dis == 0:
                    ans.append(l)
                
                if s[l] in countP:
                    countP[s[l]] += 1
                    
                    if countP[s[l]] == 1:
                        dis += 1
                l += 1
                r += 1
        return ans 