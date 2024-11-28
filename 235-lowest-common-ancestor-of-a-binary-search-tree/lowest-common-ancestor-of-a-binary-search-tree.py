# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def dfs(node, parents, target):
            parents = list(parents)
            if not node:
                return None
            parents.append(node)
            if node == target:
                return parents

            return dfs(node.left, parents, target) or dfs(node.right, parents, target)

        parentNodesP = dfs(root, [], p)
        parentNodesQ = dfs(root, [], q)

        i, j = 0, 0

        while i < len(parentNodesP) and j < len(parentNodesQ):
            if parentNodesP[i] == parentNodesQ[j]:
                result = parentNodesP[i]
            else:
                break
            i += 1
            j += 1
        return result

        

            






        