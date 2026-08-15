from collections import Counter

"""You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. 
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks."""

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency = Counter(tasks)
        most = 0
        num_most = 0
        
        for count in frequency.values():
            most = max(count, most)
            num_most = sum(1 for c in frequency.values() if c == most)

        return max(len(tasks), (most-1) * (n+1) + num_most)
