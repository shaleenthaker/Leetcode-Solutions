import bisect
import random

"""You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. 
The probability of picking an index i is w[i] / sum(w).
- For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%)."""

class Solution:

    def __init__(self, w: list[int]):
        self.weights = w
        self.sum = sum(w)
        self.runningSum = []
        total = 0
        for num in self.weights:
            total += num
            self.runningSum.append(total)


    def pickIndex(self) -> int:
        val = random.randrange(1,self.sum+1)
        index = bisect.bisect_left(self.runningSum, val)
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()