"""You are given a non-negative integer array nums. In one operation, you must:
- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0."""

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        numZeros = 0
        for val in nums:
            if val == 0:
                numZeros += 1
        if numZeros > 0:
            return len(set(nums)) - 1
        else:
            return len(set(nums))
