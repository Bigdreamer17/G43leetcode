class Solution:
    def countTime(self, time: str) -> int:
        answer = 1

        h1, h2, c, m1, m2 = time

        if h1 == "?" and h2 == "?":
            answer *= 24
        elif h1 == "?":
            if int(h2) >= 4:
                answer *= 2
            else:
                answer *= 3

        elif h2 == "?":
            if int(h1) <= 1:
                answer *= 10
            elif h1 == "2":
                answer *= 4
        if m1 == "?" and m2 == "?":
            answer *= 60
        elif m1 == "?":
            answer *= 6
        elif m2 == "?":
            answer *= 10
        
        return answer 