Time Complexity: O(n)

1. Convert the input string s to a character array ch to allow in-place modifications.
2. Initialize Two Pointers. Initialize start at the beginning of the array (0). Initialize end at the end of the array (s.length() - 1).
3. Use a while loop to iterate as long as start is less than end.
4. Define a helper method isVowel to check if a character is a vowel (both uppercase and lowercase).
5. If the character at start is not a vowel, increment the start pointer to move to the next character.
6. If the character at end is not a vowel, decrement the end pointer to move to the previous character.
7. If both start and end point to vowels, swap these characters. Then, increment the start pointer and decrement the end pointer after the swap.
8. The loop continues to move the start and end pointers and swap vowels until start is no longer less than end.
9. After exiting the loop, convert the modified character array ch back to a string and return it.
