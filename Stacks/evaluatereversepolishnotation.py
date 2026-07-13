"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression."""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for val in tokens:
            if val in ('+', '-', '*', '/'):
                val2 = nums.pop()
                val1 = nums.pop()
                if val == '+':
                    add = val1 + val2
                    nums.append(add)
                elif val == '-':
                    sub = val1 - val2
                    nums.append(sub)
                elif val == '*':
                    mult = val1 * val2
                    nums.append(mult)
                else:
                    div = int(val1 / val2)
                    nums.append(div)
            else:
                nums.append(int(val))
        return nums.pop()