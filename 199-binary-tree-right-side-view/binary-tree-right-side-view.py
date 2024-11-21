# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return []
        results = []

        current = root
        currentLevel = deque([current])
        nextLevel = deque([])

        while currentLevel:
            while currentLevel:
                current = currentLevel.popleft()
                currRightmost = current.val

                if current.left:
                    nextLevel.append(current.left)
                if current.right:
                    nextLevel.append(current.right)
            
            results.append(currRightmost)
            currentLevel, nextLevel = nextLevel, deque([])
        
        return results
                




