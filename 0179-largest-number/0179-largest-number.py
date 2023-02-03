class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            if int(str(a) + str(b)) > int(str(b)+str(a)):
                return -1 
            else: 
                return 1 
            
        nums.sort(key=cmp_to_key(cmp)) 
        
        nums = map(str,nums) 
        
        ans = "".join(nums) 
        
        if ans.count("0") == len(ans): 
            return "0"
        return ans