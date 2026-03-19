#week04-4a.py
#LeetCode 1732
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        for gg in gain:
            H += gg
            ans = max(ans, H)
        return ans
