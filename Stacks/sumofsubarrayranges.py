"""You are given an integer array nums. 
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array."""

class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        LRMaxChoices = [[] for _ in range(len(nums))]
        LRMinChoices = [[] for _ in range(len(nums))]
        maxes = []
        mins = []
        for i in range(len(nums)):
            if not maxes:
                maxes.append(i)
                LRMaxChoices[i].append(1)
            else:
                if nums[i] > nums[maxes[-1]]:
                    while maxes and nums[i] > nums[maxes[-1]]:
                        maxes.pop()
                val = maxes[-1] if maxes else -1
                maxes.append(i)
                LRMaxChoices[i].append(i - val)
            if not mins:
                mins.append(i)
                LRMinChoices[i].append(1)
            else:
                if nums[i] < nums[mins[-1]]:
                    while mins and nums[i] < nums[mins[-1]]:
                        mins.pop()
                val = mins[-1] if mins else -1
                mins.append(i)
                LRMinChoices[i].append(i - val)
        maxes = []
        mins = []
        for i in range(len(nums)-1, -1, -1):
            if not maxes:
                maxes.append(i)
                LRMaxChoices[i].append(1)
            else:
                if nums[i] >= nums[maxes[-1]]:
                    while maxes and nums[i] >= nums[maxes[-1]]:
                        maxes.pop()
                val = maxes[-1] if maxes else len(nums)
                maxes.append(i)
                LRMaxChoices[i].append(val - i)
            if not mins:
                mins.append(i)
                LRMinChoices[i].append(1)
            else:
                if nums[i] <= nums[mins[-1]]:
                    while mins and nums[i] <= nums[mins[-1]]:
                        mins.pop()
                val = mins[-1] if mins else len(nums)
                mins.append(i)
                LRMinChoices[i].append(val - i)
        total = 0
        for i in range(len(nums)):
            total += nums[i] * LRMaxChoices[i][0] * LRMaxChoices[i][1]
            total -= nums[i] * LRMinChoices[i][1] * LRMinChoices[i][0]
        return total