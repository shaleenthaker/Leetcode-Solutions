"""Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list."""

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        output = float('inf')
        minutes = []
        for i in range(len(timePoints)):
            time = int(timePoints[i][0:2])*60 + int(timePoints[i][3:5])
            minutes.append(time)
        minutes.sort()
        for i in range(len(minutes)-1):
            output = min(output, minutes[i+1]-minutes[i])
        return min(output, minutes[0]+1440-minutes[-1]) 
