class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter()
        minRabbit = 0
        
        for ans in answers:
            if dic[ans] == 0:
                minRabbit += (ans + 1)
                dic[ans] = ans
            else:
                dic[ans] -= 1
        return minRabbit