#week05-6.py
#LeetCode 2352
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()
        for row in grid:
            counter[ tuple(row) ] += 1
        ans = 0
        for col in zip(*grid):
            ans += counter[ tuple(col) ]
        return ans
