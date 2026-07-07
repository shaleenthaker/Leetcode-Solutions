"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array."""

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNums = Counter(nums)
        length = len(nums)
        for item, count in countNums.items():
            if count > (length // 2):
                return item