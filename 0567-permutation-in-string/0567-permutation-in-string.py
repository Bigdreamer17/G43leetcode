class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a dictionary
        Count1 = {}
        
        for i in s1:
            Count1[i] = 1 + Count1.get(i, 0)
        # Initialize our pointers, window and dict_count   
        l = r = 0
        window = len(s1)
        dict_count = len(Count1)
        
        while r < len(s2):
            if s2[r] in Count1:
                Count1[s2[r]] -= 1
                if Count1[s2[r]] == 0:
                    dict_count -= 1
            if r - l + 1 < window:
                r += 1
            else:
                if dict_count == 0:
                    return True 
                if s2[l] in Count1:
                    Count1[s2[l]] += 1
                    
                    if Count1[s2[l]] == 1:
                        dict_count += 1
                l += 1
                r += 1
        return False
                
                    