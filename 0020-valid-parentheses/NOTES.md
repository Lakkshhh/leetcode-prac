Time Complexity: O(n)

1. If the length of the string is odd, return false immediately since a valid parentheses string must have an even number of characters.
2. Create an empty stack to keep track of the opening brackets.
3. Loop through each character in the string.
4. If the character c is an opening bracket ('(', '{', or '['), push it onto the stack.
5. Else, check if the stack is not empty and the top of the stack matches the corresponding opening bracket. If it matches, pop the top of the stack.
6. If it does not match or the stack is empty, return false immediately.
7. After processing all characters, check if the stack sc is empty. If the stack is empty, return true indicating the string is valid. If the stack is not empty, return false indicating the string is invalid.​
