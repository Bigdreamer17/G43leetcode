class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()
        
        return " ".join(sl[::-1])