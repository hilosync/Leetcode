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
        i = 0
        current = root
        nodeStack = [i]
        currMax = current.val

        parentMax = {i:[current,currMax]}


        while nodeStack:
            temp = nodeStack.pop()
            current = parentMax[temp][0]
            currMax = parentMax[temp][1]

            if current.val >= currMax:
                result += 1
                currMax = current.val
            
            if current.left:
                i += 1
                nodeStack.append(i)
                parentMax[i] = [current.left, currMax]

            if current.right:
                i += 1
                nodeStack.append(i)
                parentMax[i] = [current.right, currMax]


        return result







