"""The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. 
  Answers within 10-5 of the actual answer will be accepted."""
  
import heapq

class MedianFinder:

    def __init__(self):
        self.lowerhalf = []
        self.upperhalf = []

    def addNum(self, num: int) -> None:
        if len(self.lowerhalf) == 0 and len(self.upperhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
        elif len(self.lowerhalf) < len(self.upperhalf):
            if num <= self.upperhalf[0]:
                heapq.heappush(self.lowerhalf, -num)
            else:
                temp = heapq.heappop(self.upperhalf)
                heapq.heappush(self.lowerhalf, -temp)
                heapq.heappush(self.upperhalf, num)
        else:
            if num >= -self.lowerhalf[0]:
                heapq.heappush(self.upperhalf, num)
            else:
                temp = -heapq.heappop(self.lowerhalf)
                heapq.heappush(self.lowerhalf, -num)
                heapq.heappush(self.upperhalf, temp)
        
    def findMedian(self) -> float:
        if len(self.lowerhalf) == len(self.upperhalf):
            return (-self.lowerhalf[0] + self.upperhalf[0]) / 2
        elif len(self.lowerhalf) < len(self.upperhalf):
            return self.upperhalf[0]
        else:
            return -self.lowerhalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
  
