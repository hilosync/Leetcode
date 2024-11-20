class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        newStack = []

        for i in range(len(s)):
            if len(newStack) == 0:
                newStack.append(s[i])
            
            elif s[i] == ')' and newStack[-1] == '(':
                newStack.pop(-1)
            elif s[i] == '}' and newStack[-1] == '{':
                newStack.pop(-1)
            elif s[i] == ']' and newStack[-1] == '[':
                newStack.pop(-1)
            else:
                newStack.append(s[i])

        return len(newStack) == 0



            
            


        