Time Complexity: O(n)

1. 'n' stores the length of the input array h.
2. 'maxArea' is initialized to 0 to keep track of the maximum area found.
3. 'st' is a stack that will store the indices of the histogram's bars.
4. A loop iterates from 0 to n inclusive. The extra iteration (i = n) handles the remaining bars in the stack after reaching the end of the histogram.
5. currHeight is set to 0 if 'i' is 'n' (end of histogram), otherwise it's set to the height of the current bar 'h[i]'.
6. The while loop will run as long as the stack is not empty and the current height is less than the height of the bar at the index on the top of the stack.
7. Pop the top index from the stack and store it in 'top'.
8. If the stack is empty after popping, the width is 'i'. Otherwise, the width is the difference between the current index 'i' and the new top of the stack minus '1'.
9. Calculate the area using the height of the bar at index 'top' and the width.
10. Update maxArea if the calculated area is larger.
11. Push the current index i onto the stack.
12. Return the maximum rectangular area found.
