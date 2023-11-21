class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i] + word2[i])
        
        return ''.join(ans) + word1[i+1:] + word2[i+1:]