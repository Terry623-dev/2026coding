#week08-5.py
#LeetCode 704
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return 0

        for i in range(N):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == N - 1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
