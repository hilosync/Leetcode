# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currNode = root

        while currNode:
            if currNode.val < min(p.val,q.val):
                currNode = currNode.right
            elif currNode.val > max(p.val, q.val):
                currNode = currNode.left
            else:
                return currNode
        
        return None
        

        

            






        