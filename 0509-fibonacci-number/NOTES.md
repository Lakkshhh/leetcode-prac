Time complexity: O(n)

1. Using three variables: a and b, initialized to 0 and 1, represent the first two Fibonacci numbers, and sum, which stores the current Fibonacci number
2. We checks if n is equal to 0 or 1, and return n directly for base cases
3. Loop until we reach the nth Fibonacci number
4. Calculate the next Fibonacci number
5. Move 'a' to the next number in the sequence(b)
6. Move 'b' to the new Fibonacci number (sum)
7. Decrease n to eventually break the loop
8. Return the nth Fibonacci number
