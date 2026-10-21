import heapq

"""Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        largest = []
        for num in nums:
            if len(largest) >= k:
                if num > largest[0]:
                    heapq.heapreplace(largest, num)
            else:
                heapq.heappush(largest, num)
        return largest[0]