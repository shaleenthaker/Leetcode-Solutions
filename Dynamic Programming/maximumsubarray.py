"""Given an integer array nums, find the subarray with the largest sum, and return its sum."""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            if max_so_far < curr_max:
                max_so_far = curr_max
        return max_so_far