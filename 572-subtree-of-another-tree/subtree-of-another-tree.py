# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        def dfs(node, subNode):
            if not node and not subNode:
                return True
            
            if not node:
                return False
            if not subNode:
                return False
            if node.val != subNode.val:
                return False
            
            return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)

        nodeStack = deque([root])

        while nodeStack:
            curr = nodeStack.popleft()
            if curr.val == subRoot.val:
                if dfs(curr, subRoot):
                    return True
            
            if curr.left:
                nodeStack.append(curr.left)
            if curr.right:
                nodeStack.append(curr.right)
        
        return False
        

      
      # Loop through main tree, find all instances of the root of the sub tree
      # for each found instance, we want to check if the trees are equal, if they are return true, if not check next instance, if no instances, return false



        

        

        