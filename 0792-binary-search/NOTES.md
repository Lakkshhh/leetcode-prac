Time Complexity: O(log n)

1. Two integer variables, 'left' and 'right', are initialized. 'left' is set to 0 (the beginning of the array) and 'right' is set to 'nums.length - 1' (the end of the array).
2. A while loop is started that continues as long as left is less than or equal to right.
3. The middle index 'mid' is calculated to avoid potential overflow. It is the average of left and right. Using 'left + (right - left) / 2' instead of '(right + left) / 2' is a common technique to avoid potential integer overflow in languages like Java, where integers have a fixed size.
4. If the element at the middle index 'nums[mid]' is equal to the target, the method returns mid (the index of the target).
5. If 'nums[mid]' is less than the target, it means the target must be in the right half of the array. So, left is updated to 'mid + 1'.
6. If 'nums[mid]' is greater than the target, it means the target must be in the left half of the array. So, right is updated to 'mid - 1'.
7. If the loop exits without finding the target, the method returns -1, indicating that the target is not present in the array.
