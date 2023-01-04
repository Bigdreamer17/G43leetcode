class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        stringsplit = s.split()
        
        FinalAnswer =[]
        
        maxlen_word = max(len(word) for word in stringsplit)
        
        for char in range(maxlen_word):
            res = []
            
            for word in stringsplit:
                if len(word) > char:
                    res.append(word[char])
                else:
                    res.append(" ")
            
            FinalAnswer.append(res)
        
        output = []
        
        for p in FinalAnswer:
            output.append(''.join(p).rstrip())
        
        return output