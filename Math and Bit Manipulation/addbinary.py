"""Given two binary strings a and b, return their sum as a binary string."""

# Initial Solution
# class Solution:
#    def addBinary(self, a: str, b: str) -> str:
#        maxlen = max(len(a), len(b)) - 1
#        minlen = min(len(a), len(b)) - 1
#        if len(a) >= len(b):
#            large = a
#            small = b
#        else:
#            large = b
#            small = a
#        out = ''
#        carry = False
#        while minlen >= 0:
#            if large[maxlen] == '1' and small[minlen] == '1':
#                if carry:
#                    out = '1' + out
#                else:
#                    out = '0' + out
#                carry = True
#            elif large[maxlen] == '1' and small[minlen] == '0':
#                if carry:
#                    out = '0' + out
#                    carry = True
#                else:
#                    out = '1' + out
#                    carry = False
#            elif large[maxlen] == '0' and small[minlen] == '1':
#                if carry:
#                    out = '0' + out
#                    carry = True
#                else:
#                    out = '1' + out
#                    carry = False
#            else:
#                if carry:
#                    out = '1' + out
#                else:
#                    out = '0' + out
#                carry = False
#            minlen -= 1
#            maxlen -= 1
#        for i in range(maxlen, minlen, -1):
#            if large[i] == '0' and carry:
#                out = '1' + out
#                carry = False
#            elif large[i] == '0':
#                out = '0' + out
#            elif large[i] == '1' and carry:
#                out = '0' + out
#                carry = True
#            else:
#                out = '1' + out
#        if carry:
#            out = '1' + out
#        return out

# Optimal Solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry

        return bin(a)[2:]
