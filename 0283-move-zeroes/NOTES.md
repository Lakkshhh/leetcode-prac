Time Complexity: O(n)

1. Initialize a variable 'left' to keep track of the position where the next non-zero element will be moved.
2. Iterate over the indices of the 'nums' list using a for loop. 'right' represents the index of the current element being processed.
3. Check if the current element at index 'right' is not equal to zero. This condition checks for non-zero elements.
4. If the current element is non-zero, swap it with the element at index 'left'. This effectively moves non-zero elements towards the beginning of the list.
5.  Increment the 'left' pointer to mark the next position where a non-zero element should be moved.
