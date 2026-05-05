class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif s[i] == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif s[i] == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False
            



        