"""You are given a 0-indexed binary string s which represents the types of buildings along a street where:
s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.
For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings."""

class Solution:
    def numberOfWays(self, s: str) -> int:
        output = 0
        leftZeros = 0
        leftOnes = 0
        numZeros = 0
        numOnes = 0
        for char in s:
            if char == '0':
                numZeros += 1
            else:
                numOnes += 1
        for i in range(len(s)):
            if s[i] == '0':
                onesToRight = numOnes - leftOnes
                output += leftOnes * onesToRight
                leftZeros += 1
            else:
                zerosToRight = numZeros - leftZeros
                output += leftZeros * zerosToRight
                leftOnes += 1
        return output