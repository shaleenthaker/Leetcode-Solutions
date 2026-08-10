"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        nToL = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}
        output = []
        def backtracking(start, curr):
            if start >= len(digits):
                output.append(curr)
                return
            for letter in nToL[digits[start]]:
                backtracking(start+1, curr + letter)
        backtracking(0, "")
        return output