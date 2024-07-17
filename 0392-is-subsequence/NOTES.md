Time Complexity: O(n)

1. Initialize two pointers, sp and tp, to 0 to represent the starting positions of the strings s and t respectively.
2. Iterate through the characters of both strings s and t, comparing characters at the corresponding positions.
3. If a matching character is found, move the pointer in s forward.
4. Always move the pointer in t forward.
5. Check if all characters in s have been matched in t.
6. Return True if s is a subsequence of t, False otherwise.
