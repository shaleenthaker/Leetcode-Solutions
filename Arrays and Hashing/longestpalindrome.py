"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome."""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        length = 0
        odd = False
        for char, count in charCount.items():
            length += (count // 2) * 2
            if count % 2 == 1:
                odd = True
        return length + 1 if odd else length