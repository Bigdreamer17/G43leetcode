class Solution:

    def __init__(self, nums: List[int]):
        self.main_array =  nums 
        self.copy_array = list(nums) 
        
    def reset(self) -> List[int]:
        self.main_array = list(self.copy_array)
        return self.main_array

    def shuffle(self) -> List[int]:
        length = len(self.main_array)
        for i in range(length):
            index = random.randint(i, length - 1)

            self.main_array[i], self.main_array[index] = self.main_array[index], self.main_array[i]  
        return self.main_array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()