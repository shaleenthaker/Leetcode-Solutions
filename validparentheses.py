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