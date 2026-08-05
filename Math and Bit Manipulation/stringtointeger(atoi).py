"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
   If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. 
   Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result."""

class Solution:
    def myAtoi(self, s: str) -> int:
        output = 0
        i = 0
        length = len(s)
        signSeen = False
        negative = False
        leading = True
        while i < length:
            if s[i].isdigit():
                signSeen = True
                leading = False
                output *= 10
                output += int(s[i])
                i += 1
            else:
                if s[i] == '+' and not signSeen:
                    leading = False
                    signSeen = True
                    i += 1
                elif s[i] == '-' and not signSeen:
                    leading = False
                    negative = True
                    signSeen = True
                    i += 1
                elif s[i] == ' ' and leading:
                    i += 1
                else:
                    break
        if negative:
            output *= -1
        if output < (-2)**31:
            output = (-2)**31
        elif output > 2**31 - 1:
            output = 2 ** 31 - 1
        return output