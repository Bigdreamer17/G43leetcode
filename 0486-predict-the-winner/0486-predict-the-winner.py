class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Base case ;-  len(array) == 0 or Position1 == Position2
        # State ;- (Position1, position2, Turn)
        # Recurion relation ;-(Position1 + 1, Position2 - 1, Turn) 
        
        
        def rec(nums,Position1, Position2, Turn):
            if Position1 == Position2:
                return Turn * nums[Position1]

            a = Turn * nums[Position1] + rec(nums, Position1 + 1, Position2, -Turn)
            b = Turn * nums[Position2] + rec(nums, Position1, Position2 - 1, -Turn)
            return Turn * max(Turn * a, Turn * b)
        
        return rec(nums,0,len(nums)-1,True) >= 0
    
    
    
    
    