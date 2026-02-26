#week01.4.py
#LeetCode 1431
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        best = max(candies)
        for candie in candies:
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False)
        return ans
