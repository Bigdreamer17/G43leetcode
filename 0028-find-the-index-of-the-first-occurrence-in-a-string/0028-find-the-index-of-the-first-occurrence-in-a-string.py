class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1

# Using KMP
class Solution:
    def KMP(self, needle):
            n = len(needle)
            l , r = 0 , 1 
            LPS = [0 for _ in range(n)]
            
            while r < n:
                if needle[l] == needle[r]:
                    LPS[r] = l + 1
                    l += 1
                    r += 1
                    
                else:
                    if l == 0:
                        r += 1
                    else:
                        l = LPS[l - 1]
            return LPS
    def strStr(self, haystack: str, needle: str) -> int:
        
        lsp = self.KMP(needle)
        p1 = p2 = 0
        
        while p1 < len(haystack):
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            elif p2 == 0:
                p1 += 1
            else:
                p2 = lsp[p2 - 1]
                
            
            if p2 == len(needle):
                return p1 - p2
            
        return -1
