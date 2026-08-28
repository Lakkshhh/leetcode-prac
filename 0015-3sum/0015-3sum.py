class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for first_index, first_num in enumerate(nums):
            if first_num > 0:
                break
            if first_index > 0 and first_num == nums[first_index - 1]:
                continue
            left_pointer, right_pointer = first_index + 1, len(nums) - 1
            while left_pointer < right_pointer:
                three_sum = first_num + nums[left_pointer] + nums[right_pointer]
                if three_sum > 0:
                    right_pointer -= 1
                elif three_sum < 0:
                    left_pointer += 1
                else:
                    triplets.append([first_num, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
        return triplets


"""Let me first make sure I understand the problem: I need to find all unique triplets in the array that sum to zero, and the tricky part isn't really finding one triplet, it's avoiding duplicate triplets in the output. The key observation is that if I sort the array first, duplicates become adjacent to each other, which makes them much easier to skip, and sorting also lets me use a two-pointer approach instead of brute-forcing every pair, since once the array is ordered I can reason about whether my current sum is too big or too small and move pointers accordingly. So the approach is: sort the array, then fix one number at a time as I iterate through it, and for each fixed number, use two pointers starting right after it and at the end of the array, moving them toward each other based on whether the three-sum is too high or too low. If the fixed number is greater than zero I can just break out early, since the array is sorted and nothing after it could bring the sum back down to zero. To avoid duplicate triplets, I skip over repeated values both for the fixed number and for the left pointer once I've found a valid triplet, since without that I'd end up recording the same combination multiple times. One subtlety I'd point out is that the duplicate-skipping check needs the left pointer bound check as part of the same condition, otherwise I risk an index error once the pointers cross. In terms of complexity, the sort takes O(n log n), and then for each element I do a linear two-pointer scan, so the nested part is O(n squared) overall, which dominates, giving O(n squared) time total, and space is O(1) extra if I don't count the output or the sort's own space, though technically the sort itself can take O(log n) space depending on the implementation.

Brute-force triple-nested loops check every combination of three indices independently, which is O(n³) and does no reuse of work between combinations — the improvement comes from sorting first and fixing one element at a time, which reduces the remaining problem to 'find two numbers that sum to a target' on a sorted subarray, exactly the two-pointer pattern from Two Sum II, run repeatedly for each choice of the first element. Sorting also directly solves the de-duplication requirement almost for free: once sorted, duplicate values are adjacent, so I skip repeated first elements outright, and after finding a valid triplet I skip past any repeated values at both the left and right pointers before continuing, preventing the same triplet from being recorded twice. I chose sort-then-two-pointer over a hash-set-based approach (fixing one element, then hash-set lookup for the second element's complement) because the two-pointer approach makes de-duplication naturally straightforward due to sorted adjacency, whereas a hash-set version would require extra bookkeeping — like converting each found triplet to a canonical sorted tuple and storing it in a separate result set — just to catch duplicates, adding complexity without improving the time complexity. This runs in O(n²) time, dominated by the two-pointer scan running once for each of the n choices of first element, with sorting contributing a smaller O(n log n), and O(n) space for the sort itself (or O(1) if in-place sorting is used, excluding the output list, which isn't typically counted against space complexity)."""