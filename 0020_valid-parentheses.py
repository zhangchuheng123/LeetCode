class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c == ')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            elif c == ']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            elif c == '}' and (len(stack) == 0 or stack[-1] != '{'):
                return False
            else:
                stack.pop()
                
        if len(stack) == 0:
            return True
        else:
            return False
