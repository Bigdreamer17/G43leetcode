class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        stringsplit = s.split()
        
        Answer =[]
        
        maxlen_word = max(len(word) for word in stringsplit)
        
        for char in range(maxlen_word):
            res = []
            
            for word in stringsplit:
                if len(word) > char:
                    res.append(word[char])
                else:
                    res.append(" ")
            
            Answer.append(res)
        
        output = []
        
        for p in Answer:
            output.append(''.join(p).rstrip())
        
        return output