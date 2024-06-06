Time Complexity: O(n^2)

1. ​First, I sort the array in ascending order to make it easier to loop through it while avoiding duplicates.
2. Then, initialize an empty list to store the triplets that sum up to zero.
3. Iterate through the array using a for loop. Check if the current element is the same as the previous one. If it's not (or if it's the first element), proceed. This step ensures that the final list doesn't include duplicate triplets.
4. Then, initialize two pointers to find the other two elements in the triplet. The first pointer starts from i + 1 and the second pointer starts from the last element of the array.
5. The target 'sum' is set as 0 - nums[i], since nums[i] + nums[low] + nums[high] = 0.
6. Use a while loop to find pairs of elements (nums[low] and nums[high]) whose sum equals 'sum'.
7. If the sum is equal to sum, we add the triplet (nums[i], nums[low], nums[high]) to ans_arr. Then, we move low and high pointers inward, skipping any duplicates.
8. If the sum is greater than sum, we decrement high to decrease the sum.
9. If the sum is less than sum, we increment low to increase the sum.
10. After the loops, we return ans_arr containing all the unique triplets.
