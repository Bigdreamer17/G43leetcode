class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for num in arr:
            if num not in occ:
                occ[num] = 1
            occ[num] += 1

        key_ = []
        value_ = []

        for key, value in occ.items():
            key_.append(key)
            value_.append(value)

        return len(set(value_)) == len(key_)