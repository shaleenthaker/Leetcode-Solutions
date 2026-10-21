import heapq

"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequent = []
        freqMap = {}
        for num in nums:
            freqMap.setdefault(num, 0)
            freqMap[num] += 1
        for key, val in freqMap.items():
            if len(frequent) >= k:
                if freqMap[frequent[0][1]] < val:
                    heapq.heapreplace(frequent, (val, key))
            else:
                heapq.heappush(frequent, (val, key))
        output = []
        for i in range(k):
            output.append(frequent[i][1])
        return output