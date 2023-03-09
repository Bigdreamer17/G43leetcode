class Solution:
    def decodeString(self, s: str) -> str:
        # Base Case ;- if s[i] == ] return current substring
        def rec(s, i):
            res = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    sub_res, i = rec(s, i + 1)
                    res += num * sub_res
                    num = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res
        return rec(s, 0)