#week10-05.py
#LeetCode 437
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1  # 有1個初始的0

        def helper(root, total):  # 之前的 total
            if root == None:
                return 0

            total += root.val
            ans = counter[total - targetSum]  # 先從 counter 找答案

            counter[total] += 1  # 累積這個 total 的出現次數

            ans += helper(root.left, total)
            ans += helper(root.right, total)

            counter[total] -= 1  # 回溯

            return ans

        return helper(root, 0)
