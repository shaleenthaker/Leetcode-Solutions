"""Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()."""

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        curr = []
        num = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i += 1
                result += num * sign
                num = 0
                i -= 1
            elif s[i] == '(':
                curr.append((result, sign))
                result = 0
                sign = 1
            else:
                (r, q) = curr.pop()
                result = r + q * result
            i += 1
        return result
