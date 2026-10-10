"""A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days."""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        best = high
        while low <= high:
            mid = low + (high - low) // 2
            daySoFar = mid
            numDays = 0
            index = 0
            while numDays <= days-1:
                if index >= len(weights):
                    best = mid
                    high = mid - 1
                    break
                elif daySoFar >= weights[index]:
                    daySoFar -= weights[index]
                    index += 1
                else:
                    numDays += 1
                    daySoFar = mid
            if index < len(weights):
                low = mid + 1
        return best
            



                

