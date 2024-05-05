Time complexity: O(n)

1) Create an empty hash table to store elements and their indices.
2) Iterate through the array from left to right.
3) For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
4) Check if the complement exists in the hash table. If it does, we have found a solution.
5) If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its index as the value.
6) Repeat steps 3-5 until we find a solution or reach the end of the array.
7) If no solution is found, return an empty array or an appropriate indicator.
