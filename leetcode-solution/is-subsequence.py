class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(s) > len(t) : return False

        seq = 0
        for i in range(0,len(t)):
            if seq <= len(s) - 1 and s[seq] == t[i]:
                    seq += 1
        return seq == len(s)