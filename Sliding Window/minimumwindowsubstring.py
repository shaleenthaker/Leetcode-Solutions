"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique."""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""

        left = 0
        right = 0

        tFreq = {}
        for char in t:
            tFreq.setdefault(char, 0)
            tFreq[char] += 1

        windowFreq = {}
        required = len(tFreq)
        formed = 0
        minSoFar = float('inf')
        start_index = 0

        for right in range(len(s)):
            windowFreq.setdefault(s[right], 0)
            windowFreq[s[right]] += 1
            if s[right] in tFreq and windowFreq[s[right]] == tFreq[s[right]]:
                formed += 1
            while formed == required:
                if right - left + 1 < minSoFar:
                    start_index = left
                    minSoFar = right - left + 1
                if s[left] in tFreq and windowFreq[s[left]] == tFreq[s[left]]:
                    formed -= 1
                windowFreq[s[left]] -= 1
                left += 1

        return "" if minSoFar == float('inf') else s[start_index:start_index+minSoFar]