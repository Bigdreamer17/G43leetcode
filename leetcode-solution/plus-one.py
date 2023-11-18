class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int("".join([str(x) for x in digits]))+1)))