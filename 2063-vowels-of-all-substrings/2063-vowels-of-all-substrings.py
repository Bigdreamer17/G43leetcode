class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)
        numVowels = 0
        
        for i, c in enumerate(word):
            if c in vowels:
                numVowels += ((n-i) * (i+1))
        return numVowels