import heapq

"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in)."""

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = -(x*x + y*y)
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for (_, point) in heap] 
