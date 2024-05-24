Time Complexity: O(nlogn) --> Since, sort function is used.
Space Complexity:O(n)​

1. Initialize a HashMap to count the frequency of each number.
2. Iterate through the array and update the frequencies in the HashMap.
3. Extract unique numbers from the HashMap's keys and store them in a list.
4. Sort the list based on frequency in descending order. Thus, created a comparator here, took two objects and comparing their frequencies, so I am sortng it based on the elemets frequencies. Hence, out of the 2, the one with higher frequency is displayed first.
5. Create an array to store the top k frequent elements.
6. Copy the first k elements from the sorted list to the array.
7. Return the array containing the top k frequent elements.
