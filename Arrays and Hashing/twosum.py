"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenVals = {}
        for i, num in enumerate(nums):
            if target - num in seenVals: # if ___ in ____ for a dict checks if the key is in the dict; value is not looked at
                return [seenVals[target - num], i] 
            seenVals[num] = i # We set the key to the number in the array, and the value to the index, since we are returning the index
            # If we wanted to return value, we would use the index as they key
        