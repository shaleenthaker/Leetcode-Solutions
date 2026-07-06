"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = self.climbStairs(1)
        b = self.climbStairs(2)
        for i in range (1, n-1):
            a, b = b, a + b
        return b