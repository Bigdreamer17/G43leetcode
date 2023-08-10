class Solution:
    def finalString(self, s: str) -> str:
        reverse = ""
        
        for character in s:
            if character == 'i':
                reverse = reverse[len(reverse)::-1]
                
            else:
                reverse += character
        return reverse