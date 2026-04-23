#week09-2.py
#LeetCode 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append( head.val )
            head = head.next
        now = ans = ListNode()
        N = len(a)
        for i in range(N-1, -1, -1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
