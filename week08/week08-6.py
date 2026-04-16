#week08-6.py
#LeetCode 875
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            total = 0
            for pile in piles:
                total += pile // k
                if pile % k > 0: total += 1
            return total <= h
        return bisect_left( range(1,max(piles)), True, key=helper) + 1
