class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        triad = []
        for num in nums:
            if len(triad) == 3:
                return True 
            elif not triad or triad[-1] < num:
                triad.append(num)
            else:
                for i, triad_member in enumerate(triad):
                    if triad_member > num:
                        triad[i] = num
                        break
                    elif triad_member == num:
                        break
        return len(triad) == 3