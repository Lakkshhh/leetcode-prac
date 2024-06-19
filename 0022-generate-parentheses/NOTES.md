Time Complexity(Rough Estimate): O(2^2n). At each step, we have two choices: add an open parenthesis ( or a close parenthesis ). We need to make these choices 2n times and there are 2^2n combinations of choosing ( or ).​ However, considering only valid parentheses pairs, the time complexity is more accurately reflected by the Catalan number: Time Complexity (Catalan Estimate): O(4^n/n^(3/2)).

Space Complexity: O(n) for the call stack, and O(4^n/n^(3/2)) for storing the results.

Backtracking problems follow a template of recursively exploring all potential solutions by making a series of decisions. The algorithm includes a base case to add valid solutions to the result list. During each recursive call, it explores one decision at a time and calls itself to build the solution further. If a decision leads to an invalid path, the algorithm backtracks by undoing the last decision and trying the next possibility. This method efficiently prunes the solution space, ensuring only viable solutions are considered.

1. Create a list res to store the resulting valid combinations of parentheses.
2. Call the backtrack function with initial parameters: an empty string s, and both open and close set to 0.
Backtracking Function:

Base Case: If the length of the string s is equal to n * 2, add s to the result list res and return.
Decision 1 (Add '('): If open is less than n, add '(' to s, increment open, and recursively call backtrack.
Decision 2 (Add ')'): If close is less than open, add ')' to s, increment close, and recursively call backtrack.
Generate Combinations:

Recursively build the string by adding valid '(' and ')' characters until the base case is met for each valid combination.
Return the Result:

Return the list res containing all valid combinations of parentheses.
