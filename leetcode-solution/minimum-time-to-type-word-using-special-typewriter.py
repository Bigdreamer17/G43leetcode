class Solution:
    def minTimeToType(self, word: str) -> int:
        minimum_seconds = len(word)
        pointer = 'a'

        for wor in word:
            value = (ord(wor) - ord(pointer)) % 26
            minimum_seconds += min(value, 26 - value)
            pointer = wor
        return minimum_seconds
         