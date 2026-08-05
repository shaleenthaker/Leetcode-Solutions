"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation."""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}
        def canBreak(start):
            if start in memo:
                return memo[start]
            if start >= len(s):
                return True
            for word in wordDict:
                if s[start:start+len(word)] == word and canBreak(start+len(word)):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        return canBreak(0)