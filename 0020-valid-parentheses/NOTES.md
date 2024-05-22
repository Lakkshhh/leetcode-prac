Time Complexity: O(n)

1. Initialized an empty stack.
2. Created a for loop to iterate through the input string character by character.
3. If the current character is an opening bracket, push it onto the stack.
4. If the current character is a closing bracket, check if the stack is empty. If it is empty, return false, because the closing bracket does not have a corresponding opening bracket. Otherwise, pop the top element from the stack and check if it matches the current closing bracket. If it does not match, return false, because the brackets are not valid.
5. After traversing the entire input string, if the stack is empty, return true, because all opening brackets have been matched with their corresponding closing brackets. Otherwise, return false, because some opening brackets have not been matched with their corresponding closing brackets.​
