Time Complexity: O(n)

1. Trim the Input String. The trim() method removes any leading and trailing whitespace from the string s. This ensures that there are no trailing spaces which could interfere with finding the last word.
2. Initialize the length variable to 0, it will keep track of the length of the last word.
3. Iterate Backwards Through the String.
4. For each character, check if it is not a space (s.charAt(i) != ' '). If it is not a space, increment the length variable.
5. If a space is encountered and the length variable is greater than 0, break the loop. This condition ensures that we stop counting once we've found a word and then encounter a space, indicating the end of the last word.
6. After the loop completes, return the value of the length variable, which now contains the length of the last word in the string.
