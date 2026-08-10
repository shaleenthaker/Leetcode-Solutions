"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order."""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        length = len(p)
        sLen = len(s)
        output = []
        pFreq = {}
        for char in p:
            if char in pFreq:
                pFreq[char] += 1
            else:
                pFreq[char] = 1
        numMatches = len(pFreq)
        matches = 0
        sFreq = {}
        for i in range(sLen):
            if i >= length:
                if s[i-length] in pFreq and pFreq[s[i-length]] == sFreq[s[i-length]]:
                    matches -= 1
                sFreq[s[i-length]] -= 1
                if s[i-length] in pFreq and pFreq[s[i-length]] == sFreq[s[i-length]]:
                    matches += 1
            if s[i] in sFreq:
                if s[i] in pFreq and pFreq[s[i]] == sFreq[s[i]]:
                    matches -= 1
                sFreq[s[i]] += 1
            else:
                sFreq[s[i]] = 1 
            if s[i] in pFreq and pFreq[s[i]] == sFreq[s[i]]:
                matches += 1
            if i >= length - 1 and matches == numMatches:
                output.append(i-length+1)
        return output