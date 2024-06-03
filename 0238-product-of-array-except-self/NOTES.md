Time Complexity: O(n) 
Space Complexity: O(n)

1. Create an array ans of the same length as the input array nums to store the results.
2. Initialize the first element of ans to 1 because there is nothing to multiply on the left side on the first element in the array.
3. Iterate through the input array nums from the second element to the last.
4. For each element at index i, set ans[i] to be the product of all elements to the left of i in nums. This is done by multiplying the previous element in ans by the previous element in nums.
5. Initialize a variable R to 1, which will store the product of all elements to the right of the current element.
6. Iterate through the input array nums from the last element to the first.
7. For each element at index i, multiply the current value in ans[i] (which currently holds the product of all elements to the left of i) by R.
8. Update R to be the product of itself and the current element in nums.
9. After completing the second iteration, ans contains the product of all elements except the current element for each position in the input array. Return the ans array.​
