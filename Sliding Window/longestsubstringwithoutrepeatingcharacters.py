"""Given a string s, find the length of the longest substring without duplicate characters."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}                                   # char -> most recent index
        slow = 0                                    # left edge of the current window
        longest = 0                                 # running max
        for fast in range(len(s)):                  # fast walks every index only once (O(n))
            ch = s[fast] 
            if ch in seen and seen[ch] >= slow:
                slow = seen[ch] + 1                 # jump left edge of window past the old copy
            seen[ch] = fast
            longest = max(longest, fast - slow + 1) # window size
        return longest
