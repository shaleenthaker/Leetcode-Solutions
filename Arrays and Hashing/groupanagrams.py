"""Given an array of strings strs, group the anagrams together. You can return the answer in any order."""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strDict = {}
        output = []
        for val in strs:
            key = ''.join(sorted(val))
            strDict.setdefault(key, []).append(val)
        for key in strDict:
            output.append(strDict[key])
        return output          