class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count, left = 0, 0
        mapp = {x:0 for x in "abc"}
        for right in range(0,len(s)):
            mapp[s[right]] += 1
            
            while mapp["a"] and mapp["b"] and mapp["c"]:
                mapp[s[left]] -= 1
                left += 1
            
            count += left        
        return count