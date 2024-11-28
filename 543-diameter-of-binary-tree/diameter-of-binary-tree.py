# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        nodeStack = [root]
        nodeDict = {None: (0, 0)}

        while nodeStack:
            curr = nodeStack[-1]
            if curr.left and curr.left not in nodeDict:
                nodeStack.append(curr.left)
                curr = curr.left
            elif curr.right and curr.right not in nodeDict:
                nodeStack.append(curr.right)
                curr = curr.right
            else:
                curr = nodeStack.pop()

                leftHeight, leftDiameter = nodeDict[curr.left]
                rightHeight, rightDiameter = nodeDict[curr.right]

                currHeight = max(leftHeight, rightHeight) + 1
                maxDiameter = max(leftHeight + rightHeight, leftDiameter, rightDiameter)

                nodeDict[curr] = (currHeight, maxDiameter)
        
        return nodeDict[root][1]





