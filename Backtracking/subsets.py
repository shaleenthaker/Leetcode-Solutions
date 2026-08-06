"""Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order."""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        def backtrack(start, curr):
            output.append(curr.copy())
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
                
        backtrack(0, [])
        return output