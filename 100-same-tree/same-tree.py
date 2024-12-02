# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        pStack = [p]
        qStack = [q]

        while pStack and qStack:
            pCurr = pStack.pop()
            qCurr = qStack.pop()
            print(pCurr.val, qCurr.val)

            if pCurr.val != qCurr.val:
                return False
            
            if (pCurr.right and not qCurr.right) or (not pCurr.right and qCurr.right) or (pCurr.left and not qCurr.left) or (not pCurr.left and qCurr.left):
                return False
            if pCurr.right:
                pStack.append(pCurr.right)
            if pCurr.left:
                pStack.append(pCurr.left)
            if qCurr.right:
                qStack.append(qCurr.right)
            if qCurr.left:
                qStack.append(qCurr.left)


        if not pStack and not qStack:
            return True
        else:
            print('4')
            return False
            


            