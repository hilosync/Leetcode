# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        current = root
        nodeStack = [current]

        while nodeStack or current:
            while current:
                nodeStack.append(current)
                current = current.left
            current = nodeStack.pop()

            k -= 1
            if k == 0:
                return current.val
            
            current = current.right
