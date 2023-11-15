class Solution:
    def conversion(self, time):
        hour, minutes  = map(int, time.split(":"))

        total_min = hour * 60 + minutes

        return total_min

    def findMinDifference(self, timePoints: List[str]) -> int:
        total_minutes  = [self.conversion(time) for time in timePoints]


        total_minutes.sort()

        min_difference = min((y - x) % (24 * 60) for x, y in zip(total_minutes, total_minutes[1:] + [total_minutes[0] + 24 * 60]))

        return min_difference