class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern_hash = Counter(pattern)
        s_hash = Counter(s)
        both = Counter(zip(pattern, s))
        if len(pattern_hash) == len(s_hash) == len(both) and len(pattern) == len(s):
            return True
        else:
            return False