#week11-5.py
#LeetCode 199
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(root, level):  # 幾層
            if root == None:
                return  # 沒有東西，就不要再函式呼叫函式

            if len(ans) <= level:  # 如果格子不夠
                ans.append(root.val)  # 新 append() 再多1格
            else:
                ans[level] = root.val  # 就直接改「那一格」

            helper(root.left, level + 1)   # 函式呼叫函式
            helper(root.right, level + 1)  # 函式呼叫函式

        helper(root, 0)

        return ans
        return ans
