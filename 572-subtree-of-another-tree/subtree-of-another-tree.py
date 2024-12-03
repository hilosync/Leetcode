# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        nodeStack = [root]
        possibleStartNodes = []
        while nodeStack:
            curr = nodeStack.pop()
            if curr.val == subRoot.val:
                possibleStartNodes.append(curr)
            if curr.left:
                nodeStack.append(curr.left)
            if curr.right:
                nodeStack.append(curr.right)

        def dfs(root, subRoot):
            if not subRoot and not root:
                return True

            if not subRoot or not root or root.val != subRoot.val:
                return False

            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
        for curr in possibleStartNodes:
            if dfs(curr, subRoot):
                return True
        return False

        

        

        