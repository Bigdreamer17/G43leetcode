class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        if diff == 2:
            return Counter(goal) == Counter(s)
        elif diff == 0:
            return not len(set(goal)) == len(goal)
        else:
            return False