Time complexity: O(logn)

1. low is initialized to the first index of the array.
2. high is initialized to the last index of the array.
3. The loop continues as long as low is less than high.
4. mid is the middle index between low and high. This avoids potential overflow issues compared to (low + high) / 2.
5. If nums[mid] is less than nums[high], it means the smallest value must be in the left half (including mid), so high is updated to mid.
6. Otherwise, the smallest value is in the right half (excluding mid), so low is updated to mid + 1.
7. When the loop ends, low will point to the smallest element in the array. Thus, nums[low] is returned.
