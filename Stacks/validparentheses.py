"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type."""

from collections import deque # Deque is an optimized python stack that makes push and pop always O(1)

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(', ']' : '[', '}' : '{'} # Use a dict of pairs so that lookup is O(1) and we don't have to individually check each possible pair
        stack = deque()
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False # If it is a closing parentheses, top item on stack should be matching open parentheses
            else:
                stack.append(char) # Push open parentheses
        return not stack # Only return true if stack is empty