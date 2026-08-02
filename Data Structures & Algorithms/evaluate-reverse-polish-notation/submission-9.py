class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                c = a + b
                stack.append(c)
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b - a
                stack.append(c)
            elif token == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                c = a * b
                stack.append(c)
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                c = b / a
                stack.append(c)
            else:
                stack.append(token)
        return int(stack[0])
                
        