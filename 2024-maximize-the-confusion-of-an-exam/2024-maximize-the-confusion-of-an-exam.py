class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        
        def find_longest(target):
            left = ans = curr = 0
            
            for right in range(n):
                if answerKey[right] == target:
                    curr += 1
                
                while left <= right and curr > k:
                    if answerKey[left] == target:
                        curr -= 1    
                    left += 1
                
                ans = max(ans, right - left + 1)
            
            return ans
        
        return max(find_longest("T"), find_longest("F"))