class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        merged = s + t
        merged_dict = {}
        for i in merged:
            if i in merged_dict:
                merged_dict[i] += 1
            else:
                merged_dict[i] = 1
        for key, value in merged_dict.items():
            if value % 2 == 1:
                return key