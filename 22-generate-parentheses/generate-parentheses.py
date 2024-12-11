class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        root = Node('(')
        def generateTree(node, opens, closes):
            if opens > 0:
                node.left = Node("(")
                generateTree(node.left, opens-1, closes)
            if closes > 0 and opens < closes:
                node.right = Node(")")
                generateTree(node.right, opens, closes-1)

            return node
        
        tree = generateTree(root, n-1, n)

        results = []
        def dfs(node, bracketsCombo):
            nonlocal results

            bracketsCombo = bracketsCombo + node.val

            if len(bracketsCombo) == 2 * n:
                results.append(bracketsCombo)

            if node.left:
                dfs(node.left, bracketsCombo)
            if node.right:
                dfs(node.right, bracketsCombo)
        
        dfs(tree, '')
        return results



