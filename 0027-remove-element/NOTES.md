Time Complexity: O(n)

1. Initialize index to 0, which represents the current position for the next non-target element.
2. Iterate through each element of the input array using the i pointer.
3. For each element nums[i], check if it is equal to the target value.
4. If nums[i] is not equal to val, it means it is a non-target element.
5. Set nums[index] to nums[i] to store the non-target element at the current index position.
6. Increment index by 1 to move to the next position for the next non-target element.
7. Continue this process until all elements in the array have been processed.
8. Finally, return the value of index, which represents the length of the modified array.
