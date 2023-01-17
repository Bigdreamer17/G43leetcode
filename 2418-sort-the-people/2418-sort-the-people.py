class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Selection sort
        for i in range(len(heights)):
            curr_max = heights[i]
            for j in range(i + 1, len(heights)):
                if heights[j] > curr_max:
                    curr_max = heights[j]
                    heights[j], heights[i] = heights[i], heights[j]
                    names[j], names[i] = names[i], names[j]
        return names