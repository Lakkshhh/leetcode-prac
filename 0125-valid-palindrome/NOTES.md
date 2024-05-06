Time Complexity: O(n)

1) Utilized a two-pointer technique: one at the start and one at the end, converging towards the middle of the string.
2) Employed a while loop to iterate until pointers meet in the middle.
3) Checked characters at pointer positions, moving pointers past non-alphanumeric characters.
4) Lowercased and compared characters, returning false if unequal.
5) Advanced pointers towards the middle if characters were equal.
6) Returned true if pointers converged, indicating a palindrome.
