class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # Pre-multiple 
        p=[nums[0]]  
        for i in range(1,n):
	        p.append(p[i-1]*nums[i])
        
        
        s=[0]*(n-1)
        s.append(nums[n-1])
        
        for i in range(n-2,-1,-1):
	        s[i]=(s[i+1]*nums[i])


        ans=[s[1]]

        for i in range(1,n-1):
	        ans.append(p[i-1]*s[i+1])

        ans.append(p[n-2])
        

        return ans