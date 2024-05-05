Time complexity: O(n)

​1) Construct an empty dictionary for storing elements and their positions.
2) Move through the array from left to right.
3) For each element nums[i] find the complement by deducting it from the target: complement = target – nums[i].
4) Verify if the complement exists in the hash table. If yes, we have a solution.
5) If not, add the current element nums[i] to the hash table with index as a value.
6) Repeat steps 3-5 until we find a solution or reach the end of the array.
7) If no solution is found, return an empty list or whatever is appropriate.
