"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order."""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        def backtracking(start, curr):
            output.append(curr.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtracking(i+1, curr)
                curr.pop()
        backtracking(0,[])
        return output