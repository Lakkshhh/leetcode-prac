Time Complexity: O(1)
Space Complexity: O(n)

Using two stacks keeps the logic straightforward and clear. Each stack has a well-defined purpose: one for the actual values and one for tracking the minimums. This separation of concerns makes the implementation easier to understand and maintain.

1. Created 2 stacks, first one to hold all the elements and the second one to hold the minimum values.
2. When a new value val is pushed, it is always added to the stack.
3. If "min_vals" stack is empty or the new value is less than or equal to the current minimum (top of min_vals), it is also pushed onto the "min_vals" stack.
4. When the top value is popped from stack, check if it is also the top of the "min_vals" stack. If it is, pop it from "min_vals" as well, which will give us the new minimum value at the top of the "min_vals" stack.
5. For the Top Operation, simply return the top value of stack.
6. For the Minimum Operation (getMin()), return the top value of the "min_vals" stack, which is the current minimum.
