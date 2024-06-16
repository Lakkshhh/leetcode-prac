Time Complexity: O(n)

1. Start by initializing an empty stack. The stack is used to store the numbers in the expression.
2. Then iterate through each token in the input array. Each token is either an operator (+, -, *, /) or a number.
3. If the token is a number, push it onto the stack.
4. If the token is an operator, pop the top two elements from the stack, perform the operation, and push the result back onto the stack. Note that the order of the operands matters for subtraction and division.
5. After all tokens have been processed, the final result of the expression is on the top of the stack. Return this result.​
