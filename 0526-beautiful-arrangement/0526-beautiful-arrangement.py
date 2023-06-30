class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1,n+1)]

        def backtrack(nums,path,index):
            if len(path) == n: res.append(path)

            for i in range(len(nums)):
                if (index + 1) % nums[i] == 0 or nums[i] % (index + 1) == 0:
                    backtrack(nums[:i] + nums[i+1:], path+ [nums[i]] , index+1)

        res = []
        backtrack(nums,[],0)

        return len(res)