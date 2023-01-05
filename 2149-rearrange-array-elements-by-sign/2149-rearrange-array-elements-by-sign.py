class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postiveNums = []
        negativeNums = []
        modifedArray = []
        postivePointer = 0
        negativePointer = 0
        
        for i in nums:
            if i >= 0:
                postiveNums.append(i)
            else:
                negativeNums.append(i)
        while postivePointer < len(postiveNums) and negativePointer < len(negativeNums):
            modifedArray.append(postiveNums[postivePointer])
            modifedArray.append(negativeNums[negativePointer])
            postivePointer += 1
            negativePointer += 1
        return modifedArray