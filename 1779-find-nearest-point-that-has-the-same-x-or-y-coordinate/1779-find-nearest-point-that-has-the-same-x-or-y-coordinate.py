class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_distance = []
        # create dictionary with valid distance as key and Manhattan distance as value
        dic = {}
        
        for i in range(len(points)):
            # Find valid points
            if x == points[i][0] or y == points[i][1]:
                valid_distance.append(points[i])
        
        if len(valid_distance) == 0:
            return -1
        
        for x1, y1 in valid_distance:
            dic[(x1, y1)] = abs(x - x1) + abs(y - y1)
         
        # get index of valid point for minimum Manhattan distance
        return points.index(list(min(dic, key=dic.get)))
        