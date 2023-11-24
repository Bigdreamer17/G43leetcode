class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        

        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str not in counter:
                counter[sorted_str] = []

            counter[sorted_str].append(string)


        return counter.values()