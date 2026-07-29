"""Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order."""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        curr = []
        used = [False] * len(nums)
        def onePerm():
            if len(curr) == len(nums):
                output.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i] == False:
                    used[i] = True
                    curr.append(nums[i])
                    onePerm()
                    curr.pop()
                    used[i] = False
        onePerm()
        return output