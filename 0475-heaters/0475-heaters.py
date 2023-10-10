class Solution:
    def binarySearch(self, heater, targetValue):
        heater.sort()
        l , r = -1, len(heater)
        
        while r > l + 1:
            mid = (r + l) // 2
            
            if heater[mid] <= targetValue:
                l = mid 
            else:
                r = mid
            
        return r
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_radius = float('-inf')
        
        for i in range(len(houses)):
            index = self.binarySearch(heaters, houses[i])
            
            if index == len(heaters):
                minn = abs(houses[i] - heaters[index - 1])
            else:
                minn = min(abs(houses[i] - heaters[index]), abs(houses[i] - heaters[index - 1]))
            
            max_radius = max(max_radius, minn)
            
        return max_radius