#week04-5.py
#LeetCode 724
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] )
        postfix = [0] * (N+1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        return -1
