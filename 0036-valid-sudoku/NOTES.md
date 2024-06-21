Time Complexity: O(n^2) but its basically O(1) due to the small fixed size of the sudoku.

1. Using a HashSet to keep track of seen numbers in rows, columns, and sub-boxes.​
2. Thetwo nested loops iterate over each cell of the 9×9 Sudoku board.
3. If the current cell contains a digit (not a '.'), it performs validation checks.
4. Construct unique strings to represent the current number's position in its row, column, and sub-box.
5. The 'add' feature of hashset returns true if the element is not already present in the hashset, and false if it already exisit. We will use this feature to our advantage.
6. Try to add these strings to the HashSet. If any add operation returns false, it means the number has already been seen in that specific row, column, or sub-box, thus the board is invalid.
7. If the loops complete without finding any duplicates, the board is valid.
