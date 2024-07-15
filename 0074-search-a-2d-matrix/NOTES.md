Time Complexity: O(log(m×n))

1. Determine the number of rows (rows) and columns (cols) in the matrix.
2. Set the initial values of 'left' to 0 and 'right' to the total number of elements in the matrix minus one (rows * cols - 1).
3. While left is less than or equal to right: Calculate the middle index (mid) of the current search range.
4. Determine the row and column corresponding to the middle index.
5. row = mid / cols: Integer division to get the row index because it tells us how many full rows fit into mid.
6. col = mid % cols: Modulo operation to get the column index, which tells us the position within the row.
7. Retrieve the element at the calculated row and column (guess = matrix[row][col]).
8. Compare guess with the target.
9. If guess is equal to the target, return true.
10. If guess is less than the target, adjust 'left' to 'mid + 1' to search in the right half.
11. If guess is greater than the target, adjust 'right' to 'mid - 1' to search in the left half.
12. If the target is not found by the end of the loop, return false.
