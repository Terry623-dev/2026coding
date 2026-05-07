#week11-4.py
#LeetCode 450
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root):  # 找到左邊的最右邊
            if root.right == None:
                return root.val
            return helper(root.right)

        if root == None:
            return root

        if root.val == key:
            if root.left == None:
                return root.right  # 接右邊

            key2 = helper(root.left)
            root.val = key2
            root.left = self.deleteNode(root.left, key2)
            return root

        if root.left:
            root.left = self.deleteNode(root.left, key)

        if root.right:
            root.right = self.deleteNode(root.right, key)

        return root
