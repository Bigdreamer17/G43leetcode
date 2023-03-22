class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        final = [0]*(len(s)+1)

        for shift in shifts:            
            final[shift[0]] += 1 if shift[2]==1 else -1
            final[shift[1]+1] += -1 if shift[2]==1 else 1

        res = []
        cum = 0

        for i in range(len(final)-1):

            cum += final[i]
            new_idx = (ord(s[i]) + cum%26)
            new_idx -= 26 if new_idx>122 else 0
            res.append(chr(new_idx))

        return "".join(res)
        