from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenVals = {}
        for i, num in enumerate(nums):
            if target - num in seenVals:
                return [seenVals[target - num], i]
            seenVals[num] = i
        