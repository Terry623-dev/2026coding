#week11-3.py
#LeetCode 700
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root==None: return None
            if val < root.val:
                return helper(root.left, val)
            if val > root.val:
                return helper(root.right, val)
            if val == root.val:
                return root

        return helper(root, val)
