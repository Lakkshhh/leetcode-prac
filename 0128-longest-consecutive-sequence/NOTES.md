Time Complexity: O(n)

1. Create a HashSet to store unique numbers from the list.
2. Iterate through the list and add each number to the HashSet.
3. Initialize a variable max_sequence_length to keep track of the longest sequence found.
4. While iterating through each number in the list, check if the number one less than the current number is not in the HashSet (indicating the start of a new sequence).
5. If so, start a new count from this number and incrementally check for consecutive numbers in the HashSet.
6. Keep track of the length of the current sequence.
7. Update max_sequence_length if the current sequence is longer than the previously recorded sequences.
8. Return the value of max_sequence_length which holds the length of the longest consecutive sequence found.​
