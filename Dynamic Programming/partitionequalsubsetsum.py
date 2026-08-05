"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise."""

# Initial attempt: forwards dp, memory inefficient
# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         total = sum(nums)
#         if total % 2 != 0:
#             return False
#         memo = {}
#         def isHalf(start, remaining):
#             if (start, remaining) in memo:
#                 return memo[(start, remaining)]
#             elif remaining == 0:
#                 memo[(start, remaining)] = True
#                 return True
#             elif remaining < 0 or start >= len(nums):
#                 memo[(start, remaining)] = False
#                 return False
#             result = isHalf(start+1, remaining - nums[start]) or isHalf(start+1, remaining)
#             memo[(start, remaining)] = result
#             return result
#         return isHalf(0, total // 2)

# Optimal solution (backwards dp storing results in a flat 1-D array)
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]