from collections import Counter

"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array."""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        countNums = Counter(nums)
        length = len(nums)
        for item, count in countNums.items():
            if count > (length // 2):
                return item