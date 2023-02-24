class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        mono = []
        for i in range(len(number)):
            if number[i] == digit:
                val = int(number[:i] + number[i+1:])
                mono.append(val)
        return str(max(mono))