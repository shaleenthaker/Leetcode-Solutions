from collections import Counter

"""Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible."""

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        ranked_list = freq_map.most_common()
        if ranked_list[0][1] > (len(s)+1) // 2:
            return ""
        reorganized = [0] * len(s)
        index = 0
        for i in range(len(ranked_list)):
            for j in range(ranked_list[i][1]):
                reorganized[index] = ranked_list[i][0]
                index += 2
                if index >= len(s):
                    index = 1
        return ''.join(reorganized)
