class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        pt = 0
        while pt < len(command):
            if command[pt] == 'G':
                ans.append('G')
            if command[pt] == '(' and command[pt + 1] == ')':
                ans.append('o')
            if command[pt] == '(' and command[pt + 1] == 'a':
                ans.append('al')
            pt += 1
        return ''.join(ans)