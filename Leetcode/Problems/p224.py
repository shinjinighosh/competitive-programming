# 224. Basic Calculator


'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

Understand:
- evaluate a string with (), +-, whitespaces and +ve ints
- function to accept string -> discard spaces ->
  -> identify numerals/operators -> apply in correct order -> return
- example: "12-(3-8)+   (  (11-7)+4)  "
            -> 12-(3-8)+((11-7)+4)
            -> 12-[-5]+(4+4)
            -> 12-[-5]+8
            -> 25
Match:
- data structure: stack
- use lambdas to map operators to functions

Plan / Pseudocode:
- create the hash table to map operators to functions
  add: lambda x,y: x + y
  sub: lambda x,y: x - y
- iterate through the string and push the operators and operands into a stack as ints of whole numbers/operators
  - if whitespace: continue
  - if ')', pop from the stack until the most recent 2 operands and one operator -> evaluate through hash table -> push result back to stack
    - terminate until you find '(' and pop it

while len(stack) > 1:
  evaluate by popping recent 2 operands and one operator

return stack.pop()

'''
operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y}


def evaluateLinear(q):
    if len(q) == 1:
        return q.pop()
    print("eval: ", q)
    value = q.pop()
    while q:
        operator = q.pop()
        value = operators[operator](value, q.pop())
    return value


def calculate(s):

    stack = []
    temp_num = ''
    for c in s:
        print(stack, temp_num)
        if c == ' ':
            continue
        elif c in '+-':
            if temp_num:
                stack.append(int(temp_num))
            temp_num = ''
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            if temp_num:
                q = [int(temp_num)]
            while stack[-1] != '(':
                q.append(stack.pop())
            stack.pop()
            stack.append(evaluateLinear(q))
            temp_num = ''
        else:
            temp_num += c
    if temp_num:
        stack.append(int(temp_num))
    return evaluateLinear(stack[::-1])

# print(calculate("12-(3-8)+   (  (11-7+5)+4)  "))
# print(calculate(" 2-1 + 2 "))


print(calculate("(1-(3-4))"))

'''
operators = {'+': lambda x, y: x+y,
              '-': lambda x, y: x-y}

def evaluateLinear(q):
    value = q.pop()
    while q:
        operator = q.pop()
        value = operators[operator](value, q.pop())
    return value

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        temp_num = ''
        for c in s:
            if c == ' ':
                continue
            elif c in '+-':
                if temp_num:
                    stack.append(int(temp_num))
                temp_num = ''
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                if temp_num:
                    q = [int(temp_num)]
                while stack[-1] != '(':
                    q.append(stack.pop())
                stack.pop()
                stack.append(evaluateLinear(q))
                temp_num = ''
            else:
                temp_num += c
        if temp_num:
            stack.append(int(temp_num))
        return evaluateLinear(stack[::-1])


'''
