#week07-4.py
#LeetCode 394
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nowN, nowS = 0, ''
        for c in s:
            if c.isdigit():
                nowN = nowN * 10 + int(c)
            elif c.isalpha():
                nowS += c
            elif c=='[':
                stack.append((nowN,nowS))
                nowN, nowS = 0, ''
            elif c==']':
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS
        return nowS
