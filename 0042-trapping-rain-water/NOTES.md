Time Complexity : O(n)
Space Complexity: O(1)

**Basic Idea:**
The idea is to fill water between two walls. The water level can only be as high as the shorter wall. If the water level exceeds the shorter wall, it will overflow. We use two pointers, leftMax and rightMax, to track the maximum heights from the left and right, respectively. We compare the heights on each side and fill water up to the limit of the shorter side, iterating until the two pointers meet.

1. Start with two pointers: left at the beginning of the array and right at the end.
2. Initialize leftMax with the height at the left pointer and rightMax with the height at the right pointer.
3. Initialize the result res to 0, which will store the total amount of trapped water.
4. Use a while loop that continues as long as left is less than right.
5. If leftMax is less than rightMax: Move the left pointer to the right (left++).
6. Update leftMax to the maximum of the current leftMax and the height at the new left pointer.
7. Calculate the trapped water at the current left position as leftMax - height[left] and add it to res.
8. Else (if leftMax is greater than or equal to rightMax):
9. Move the right pointer to the left (right--).
10. Update rightMax to the maximum of the current rightMax and the height at the new right pointer.
11. Calculate the trapped water at the current right position as rightMax - height[right] and add it to res.
12. After the loop ends, return the accumulated result res, which contains the total amount of trapped water.
