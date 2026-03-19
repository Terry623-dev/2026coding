#week04-4c.py
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums)
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1: return nn
        return -1
