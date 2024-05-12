class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        def apply(op, a, b):
            if op == "+":
                return a + b
            elif op == "-":
                return a-b
            elif op == "*":
                return a * b
            else:
                return int(a / b)

        for elt in tokens:
            if elt in operators:
                num_2 = stack.pop()
                num_1 = stack.pop()
                res = apply(elt, num_1, num_2)
                stack.append(res)
            else:
                stack.append(int(elt))
        
        return stack[0]
                
