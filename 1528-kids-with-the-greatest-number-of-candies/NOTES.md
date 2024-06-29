Time Complexity: O(n)

1. Initialize a 
2. Find the maximum number of candies among all the kids by iterating through the candies array.
3. Iterate through the candies array again and check for each kid if they can have the greatest number of candies by adding extraCandies to their candies and comparing it to the maximum number of candies.
4. If it is greater than or equal to the maximum number of candies, add true to the result list, else add false to the result list.
5. Return the result list
