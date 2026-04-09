#week07-3.py
#LeetCode 2390
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c=='*':ans.pop()
            else: ans.append(c)
        return ''.join(ans)
