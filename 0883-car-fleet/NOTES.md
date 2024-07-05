Time Complexity: O(n)

1. Create an array times to store the time it takes for each car to reach the target. The array has a size of target + 1 to cover all possible positions up to the target.
2. Iterate through the position array. For each car, calculate the time it takes to reach the target and store it in the times array at the index corresponding to the car's position.
3. (target - position[i]) gives the distance remaining for the car to reach the target. Dividing this distance by speed[i] gives the time required to reach the target.
4. Initialize previous to keep track of the time of the last fleet and fleetCount to count the number of fleets.
5. Iterate through the times array from the end (position closest to the target) to the beginning.
6. If times[i] is greater than previous, it means this car will form a new fleet because it can't catch up to the previous fleet. Update previous to the current time and increment fleetCount.
7. Finally, return the count of car fleets.
