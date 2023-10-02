class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        NotGrumpy = 0
        
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                NotGrumpy += customers[i]
        

        for i in range(minutes):
            if grumpy[i] == 1:
                NotGrumpy += customers[i]
        
        maxsum = NotGrumpy
        
        left = 0
        right = minutes
        
        while right < len(customers):
            if grumpy[right]:
                NotGrumpy += customers[right]
            if grumpy[left]:
                NotGrumpy -= customers[left]

            if NotGrumpy > maxsum:
                maxsum = NotGrumpy
            left += 1
            right += 1
        
        return maxsum
