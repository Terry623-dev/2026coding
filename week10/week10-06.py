#week10-06.py
#LeetCode 1372
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0  # 整體的答案

        def helper(root):
            if root == None:
                return 0, 0  # 左邊長, 右邊長

            lans1, lans2 = helper(root.left)
            rans1, rans2 = helper(root.right)

            self.ans = max(self.ans, lans2 + 1, rans1 + 1)

            return lans2 + 1, rans1 + 1

        helper(root)
        return self.ans - 1
