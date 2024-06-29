Time Complexity: O(n) --> Pushing and popping are constant time operations, O(1). Since each temperature index is pushed and popped from the stack at most once, the total number of operations is linear with respect to the number of temperatures.

1. Initialize an empty stack to keep track of the indices of temperatures.
2. Initialize a list of the same length as temperatures, all elements are initially already set to 0. This list will store the number of days until the next warmer temperature for each day.
3. Iterate through the temperatures list using a for loop.
4. Within the loop, we enter a while loop as long as the stack is not empty and the temperature of the current day (temps[i]) is greater than the temperature of the day represented by the index at the top of the stack (temps[index.peek()]).
5. If the condition is satisfied, we pop the index from the stack (index.pop()) and calculate the number of days until the next warmer day by subtracting the popped index from the current index i. We then update the corresponding position in the res list with this value.
6. Then, append the current index i to the stack "index".
7. Finally, return the res list containing the number of days until the next warmer temperature for each day.
