# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        result = 0
        current = root

        nodeStack = [(current, current.val)]

        while nodeStack:
            current, currMax = nodeStack.pop()

            if current.val >= currMax:
                result += 1
                currMax = current.val

            if current.left:
                nodeStack.append([current.left, currMax])
            if current.right:
                nodeStack.append([current.right, currMax])
        
        return result







