class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        
        def backtrack(idx, curr):
            string = ''.join(curr)
            if len(string) > len(set(string)):
                return
            self.max_len = max(self.max_len, len(string))
            
            for i in range(idx, len(arr)):
                backtrack(i + 1, curr + [arr[i]])
        
        backtrack(0, [])
        return self.max_len