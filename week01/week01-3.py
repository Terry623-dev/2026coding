#week01-3.py
#LeetCode 1071
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        N = gcd(N1, N2)
        ans = str1[:N]
        if ans*(N1//N) != str1: return ""
        if ans*(N2//N) != str2: return ""
        return ans
