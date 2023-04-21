class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        best, bitsets = 0, {}
        for i in range(len(words)):
            wordlen, bitset = len(words[i]), 0
            
            if wordlen * len(words[0]) < best:
                return best
            for c in words[i]:
                bitset |= 1 << ord(c) - 97
            if bitset not in bitsets:
                for k,v in bitsets.items():
                    if not bitset & k:
                        best = max(best, wordlen * v)
                bitsets[bitset] = wordlen
        return best