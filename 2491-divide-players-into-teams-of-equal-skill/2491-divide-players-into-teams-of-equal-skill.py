class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        summ = skill[0] + skill[-1]
        chem = 0
        left = 0
        right = len(skill) - 1
        
        while left <= right:
            if skill[left] + skill[right] == summ:
                product = skill[left] * skill[right]
                chem += product
            else:
                return -1
            
            left += 1
            right -= 1
        
        return chem