#week11-1a.py
#LeetCode 872
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None:
                a.append( root.val )
            if root.left: helper(root.left)
            if root.right: helper(root.right)
        helper(root1)
        a, b = [], a
        helper(root2)
        print('a',a)
        print('b',b)
        return a == b
