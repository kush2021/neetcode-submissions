class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) > 0:
                if c == ')' and stack.pop() != '(':
                    return False
                if c == ']' and stack.pop() != '[':
                    return False
                if c == '}' and stack.pop() != '{':
                    return False
            else:
                return False
        
        return len(stack) == 0