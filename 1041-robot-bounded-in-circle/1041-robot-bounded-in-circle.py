class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x =  y = i = 0
        for instruction in instructions:
            if instruction == "R":
                i = (i + 1) % 4
            elif instruction == "L":
                i = (i + 3) % 4
            else:
                x, y = x + directions[i][0], y + directions[i][1]
        return (x,y) == (0, 0) or i > 0  