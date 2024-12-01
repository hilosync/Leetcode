# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        nodeStack = [root]
        nodeDict = {None: 0}
    
        while nodeStack:
            curr = nodeStack[-1]
            if curr.left and curr.left not in nodeDict:
                nodeStack.append(curr.left)
            elif curr.right and curr.right not in nodeDict:
                nodeStack.append(curr.right)
            else:
                curr = nodeStack.pop()
                left, right = nodeDict[curr.left], nodeDict[curr.right]
                if abs(left-right) > 1:
                    return False

                nodeDict[curr] = max(left,right) + 1

        return True