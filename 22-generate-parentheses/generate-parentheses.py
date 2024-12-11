class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        brackets = []
        def recursive(opens, closes):
            if opens > closes:
                return

            if opens == closes == 0:
                results.append("".join(brackets))
                return

            if opens > 0:
                brackets.append('(')
                recursive(opens-1, closes)
                brackets.pop()
            if closes > opens:
                brackets.append(')')
                recursive(opens, closes-1)
                brackets.pop()
        
        recursive(n,n)
        return results

