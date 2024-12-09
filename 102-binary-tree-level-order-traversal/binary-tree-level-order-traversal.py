# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        currLevel = [root]
        nextLevel = []

        results = [[root.val]]

        while currLevel:
            curr = currLevel.pop(0)
            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
            
            if not currLevel and nextLevel:
                results.append([x.val for x in nextLevel])
                currLevel = list(nextLevel)
                nextLevel = []

        return results


