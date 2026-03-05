#week02-3.py
#LeetCode 392
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        if N1==0: return True
        i = 0
        for k in range(N2):

            if s[i] == t[k]:
                i += 1
            if i==N1:
                return True
        return False
