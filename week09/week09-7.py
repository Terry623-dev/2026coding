#week09-7.py
#LeetCode 2130
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append( head.val )
            head = head.next
        N = len(a)
        ans = 0
        for i in range(N):
            ans = max(ans, a[i]+a[N-1-i])
        return ans
