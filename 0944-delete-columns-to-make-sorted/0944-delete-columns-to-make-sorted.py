class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        stack = []
        for col in range(len(strs[0])):
            for row in range(len(strs)):
                if not stack:
                    stack.append(strs[row][col])
                if ord(stack[-1]) <= ord(strs[row][col]):
                    stack[-1] = strs[row][col]
                    continue
                else:
                    count += 1
                    break
            stack = []
        
        return count