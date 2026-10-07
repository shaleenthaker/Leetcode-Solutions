"""Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
Return the maximum length of a subarray with positive product."""

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        pos = 0
        neg = 0
        maxPos = 0
        for num in nums:
            if num > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif num < 0:
                tempPos = pos
                tempNeg = neg
                if tempNeg > 0:
                    pos = tempNeg + 1
                else:
                    pos = 0
                if tempPos > 0:
                    neg = tempPos + 1
                else:
                    neg = 1
            else:
                maxPos = max(pos, maxPos)
                pos = 0
                neg = 0
            maxPos = max(pos, maxPos)
        return maxPos