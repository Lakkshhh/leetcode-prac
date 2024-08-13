Time Complexity: O(n)

1. Initialize a min variable to the maximum possible value.
2. Create a maxProfit variable to track the highest profit encountered while iterating through the array.
3. Use a for loop to iterate through each element in the array.
4. Within the loop, check if the current element is less than the min variable. If it is, update min to this new value.
5. Otherwise, if the difference between the current element and min is greater than the current maxProfit, update maxProfit with this new difference.
6. After the loop, return the maxProfit variable as the result.
