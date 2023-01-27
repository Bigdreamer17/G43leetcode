class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # - for radix sorting
        base = 10 # - base in radix
        index = 0 # - index in radix
        n,m = len(nums), max(nums)
        
        while base**index < m:
            
            # - buckets
            counter = [0] * base
            
            # - distribute numbers into buckets
            for i,val in enumerate(nums):
                key = (val // (base**index)) % base
                counter[key] += 1
                
            # - calculate the "end" location of each buckets
            prefixSum = 0
            for i,val in enumerate(counter):
                prefixSum += val
                counter[i] = prefixSum
                
            # - assign numbers according to the location memorized by counter
            next_array = [0] * n
            for val in nums[::-1]:
                key = (val // (base**index)) % base
                location = counter[key]
                next_array[location-1] = val
                counter[key] -= 1
            
            # - update array 
            nums = next_array
            
            # - increase index by 1
            index += 1
        
        # - Deal with negative, same methodology, but buckets size = 2, namely [0 < val, val >= 0]
        counter = [0,0]
        for val in nums:
            if val >= 0:
                counter[1]+=1
            else:
                counter[0]+=1
        counter[1]+=counter[0]
        
        next_array = [0] * n
        for val in nums[::-1]:
            if val >= 0:
                next_array[counter[1]-1] = val
                counter[1]-=1
            else:
                next_array[counter[0]-1] = val
                counter[0]-=1
        nums = next_array
        
        return nums