from collections import deque

"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = deque()
        patterns = {}
        visited = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns.setdefault(pattern, []).append(word)
        q.append(beginWord)
        visited[beginWord] = ""
        path = 1
        while q:
            length = len(q)
            for i in range(length):
                word = q.popleft()
                if word == endWord:
                    return path
                else:
                    for j in range(len(word)):
                        pattern = word[:j] + "*" + word[j+1:]
                        if pattern in patterns:
                            for val in patterns[pattern]:
                                if val in visited:
                                    continue
                                q.append(val)
                                visited[val] = ""
            path += 1
        return 0
