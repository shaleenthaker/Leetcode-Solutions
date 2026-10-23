"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations."""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        candidates.sort()
        def backtracking(index, currSum, currList):
            if currSum == target:
                output.append(currList.copy())
                return
            for i in range(index, len(candidates)):
                if currSum + candidates[i] > target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                currList.append(candidates[i])
                backtracking(i+1, currSum + candidates[i], currList)
                currList.pop()
        backtracking(0, 0, [])
        return output