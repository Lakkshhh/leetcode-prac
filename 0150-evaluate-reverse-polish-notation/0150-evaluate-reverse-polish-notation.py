class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for val in tokens:
            if val not in {"+", "-", "*", "/"}:
                stack.append(int(val))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if val == "+":
                    stack.append(a + b)
                elif val == "-":
                    stack.append(a - b)
                elif val == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        
        return stack[0]