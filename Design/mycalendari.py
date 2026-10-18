"""You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
Implement the MyCalendar class:
- MyCalendar() Initializes the calendar object.
- boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
"""

class MyCalendar:

    def __init__(self):
        self.intervals = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        i = 0
        n = len(self.intervals)
        while i < n:
            if (startTime <= self.intervals[i][0] and endTime > self.intervals[i][0]) or (startTime > self.intervals[i][0] and startTime < self.intervals[i][1]):
                return False
            if self.intervals[i][1] <= startTime:
                self.intervals.insert(i, (startTime, endTime))
                return True
            
            i += 1
        self.intervals.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)