Time Complexity: O(n)

1. Initialize variables to keep track of the result (ans), the value of the current numeral (num), and the value of the previous numeral (prev).
2. Iterate through the string from the end to the beginning.
3. For each character, determine its value using a switch statement.
4. Compare the current numeral's value with the previous numeral's value:
5. If the current numeral is less than the previous numeral, subtract its value from answer.
6. Otherwise, add its value to answer.
7. Update the prev variable to the current numeral's value.
8. Return the final answer.
