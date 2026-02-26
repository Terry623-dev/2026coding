#week01-2.py
#LeetCode 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        N1, N2 = len(word1), len(word2)
        i, j = 0, 0
        while i<N1 or j<N2:
            if i<N1: ans += word1[i]
            if j<N2: ans += word2[j]
            i, j = i+1, j+1
        return ans
