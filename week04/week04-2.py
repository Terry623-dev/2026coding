#week04-2.py
#LeetCode 1732
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        N = len(gain)
        ans = H = 0
        for i in range(N):
            H += gain[i]
            ans = max(ans, H)
        return ans
