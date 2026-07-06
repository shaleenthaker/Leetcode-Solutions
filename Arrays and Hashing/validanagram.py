"""Given two strings s and t, return true if t is an anagram of s, and false otherwise."""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Basic solution: store s in a hashmap and compare each char in t to s
        # if len(t) != len(s):
        #     return False
        # count = {}
        # for ch in s:
        #     count[ch] = count.get(ch, 0) + 1
        # for i in t:
        #     if i not in count or count[i] <= 0:
        #         return False
        #     count[i] -= 1
        # return True
        #
        # Optimized solution: use a set (only tracks unique characters)
        if len(s) != len(t):
            return False
        setS = set(s)
        for char in setS:
            # if unique char count is not equal
            if s.count(char) != t.count(char):
                return False
        return True
        # If their lengths are equal, they can only be anagrams if they have the same number of unique chars
            