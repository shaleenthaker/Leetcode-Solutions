"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."""

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 1 or len(height) == 2:
            return 0
        total = 0
        leftMax = height[0]
        rightMax = height[len(height)-1]
        left = 1
        right = len(height) - 2
        while right >= left:
            if leftMax < rightMax:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    total += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    total += rightMax - height[right]
                right -= 1
        return total


        
