"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = -nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                target = nums[left] + nums[right]
                if target > val or right < length - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                elif target < val or left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                else:
                    out.append([-val, nums[left], nums[right]])
                    left += 1
                    right -= 1
        return out
