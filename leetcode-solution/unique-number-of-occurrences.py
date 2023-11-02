class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for a in arr:
            if a not in freq:
                freq[a] = 1
            freq[a] += 1
        values = []
        for v in freq.values():
            values.append(v)
        if len(set(values)) == len(set(arr)):
            return True
        else:
            return False