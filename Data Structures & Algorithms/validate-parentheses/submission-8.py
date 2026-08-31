class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "]":
                if len(stack) < 1:
                    return False
                a = stack.pop()
                if a != "[":
                    return False
            elif char == ")":
                if len(stack) < 1:
                    return False
                b = stack.pop()
                if b != "(":
                    return False
            elif char == "}":
                if len(stack) < 1:
                    return False
                c = stack.pop()
                if c != "{":
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
            
        