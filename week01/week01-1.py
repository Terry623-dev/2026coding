#week01-1.py
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s, 2)
        while n > 1:
            if n%2==0: n = n // 2
            else: n = n+1
            ans += 1
        return ans
