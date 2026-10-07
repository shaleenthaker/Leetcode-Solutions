"""You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.
The ith day is a good day to rob the bank if:
- There are at least time days before and after the ith day,
- The number of guards at the bank for the time days before i are non-increasing, and
- The number of guards at the bank for the time days after i are non-decreasing.
More formally, this means day i is a good day to rob the bank if and only if security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter."""

class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        if time >= len(security) / 2:
            return []
        nonincreasing = 0
        nondecreasing = 0
        output = []
        days = [[0, 0] for _ in range(len(security))] 
        for i in range(len(security)):
            if i > 0 and security[i] < security[i-1]:
                nonincreasing += 1
                nondecreasing = 1
            elif i > 0 and security[i] > security[i-1]:
                nonincreasing = 1
                nondecreasing += 1
            else:
                nonincreasing += 1
                nondecreasing += 1
            days[i][0] = nonincreasing
            days[i][1] = nondecreasing
        for i in range(time, (len(security) - time)):
            if days[i][0] > time and days[i+time][1] > time:
                output.append(i)
        return output