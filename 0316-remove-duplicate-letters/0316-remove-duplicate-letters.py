class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l = {}
        for i in range(len(s)):
            l[s[i]] = i
        stack = []
        v = set()
        
        for i in range(len(s)):
            
            if s[i] not in v:
                
                while (stack and stack[-1] > s[i] and l[stack[-1]] > i):
                    v.remove(stack.pop())
        
                stack.append(s[i])
                v.add(s[i])
        
        return ''.join(stack)