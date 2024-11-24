# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 1
        
        def dfs(node, currDepth):
            nonlocal maxDepth
            maxDepth = max(maxDepth, currDepth)
            if node.left:
                dfs(node.left, currDepth+1)

            if node.right:
                dfs(node.right,currDepth+1)

            return maxDepth
        
        return dfs(root,1)
            
            
