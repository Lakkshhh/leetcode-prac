class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        shorter_array, longer_array = nums1, nums2
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2
        if len(longer_array) < len(shorter_array):
            shorter_array, longer_array = longer_array, shorter_array

        low_partition, high_partition = 0, len(shorter_array) - 1
        while True:
            shorter_partition_index = (low_partition + high_partition) // 2
            longer_partition_index = half_length - shorter_partition_index - 2

            shorter_left_val = shorter_array[shorter_partition_index] if shorter_partition_index >= 0 else float("-infinity")
            shorter_right_val = shorter_array[shorter_partition_index + 1] if (shorter_partition_index + 1) < len(shorter_array) else float("infinity")
            longer_left_val = longer_array[longer_partition_index] if longer_partition_index >= 0 else float("-infinity")
            longer_right_val = longer_array[longer_partition_index + 1] if (longer_partition_index + 1) < len(longer_array) else float("infinity")

            if shorter_left_val <= longer_right_val and longer_left_val <= shorter_right_val:
                if total_length % 2:
                    return min(shorter_right_val, longer_right_val)
                return (max(shorter_left_val, longer_left_val) + min(shorter_right_val, longer_right_val)) / 2
            elif shorter_left_val > longer_right_val:
                high_partition = shorter_partition_index - 1
            else:
                low_partition = shorter_partition_index + 1


"""Let me first make sure I understand the problem: I've got two sorted arrays and I need to find the median of the combined array, and the naive way would be to just merge them and grab the middle, but that's O(m+n), and the fact that the problem specifically asks for log time complexity tells me it wants something better, so I need to think in terms of binary search rather than merging. The key observation is that I don't actually need to merge anything — I just need to find a partition point that splits the combined array into a left half and a right half of the correct sizes, such that every value on the left is less than or equal to every value on the right; if I can find that partition, the median just falls out of the values sitting right at the edges of the cut. So instead of picking a data structure, what I really need is a way to represent "a partition into both arrays simultaneously," and the trick is that if I decide how many elements come from the shorter array, that automatically tells me how many need to come from the longer array to make the halves the right size, so I only ever need to binary search over one array. That's why I always binary search on the shorter of the two arrays, partly for correctness — so the partition index into the longer array never goes negative or out of bounds — and partly because it keeps the search space as small as possible. So the approach is: binary search a cut point in the shorter array, derive the matching cut point in the longer array from the total length, then look at the four boundary values around both cuts — left and right of each partition — using positive or negative infinity for out-of-bounds partitions so I don't need special-case branching. If the left side of one array is ever greater than the right side of the other, that tells me my partition is unbalanced, so I shift my binary search left or right accordingly; once both cross-conditions hold, I know I've found the correct overall partition, and then the median is either the smaller of the two right-edge values if the total length is odd, or the average of the max of the left edges and the min of the right edges if it's even. In terms of complexity, this runs in O(log(min(m,n))) time since I'm only binary searching over the shorter array, and it's O(1) space since I'm just tracking a few pointers and values rather than building any new structure.

Merging both arrays and taking the middle would work but costs O(m+n), and even a two-pointer merge without full concatenation still costs O(m+n) since it has to walk up to the halfway point — the insight that beats this is that I don't actually need to merge anything, I just need to find a partition point in each array such that everything to the left of both partitions (combined) is less than or equal to everything to the right of both partitions (combined), and if such a partition exists, the median is derivable directly from the four boundary values around it. Since a valid partition point in the shorter array uniquely determines the required partition point in the longer array (their combined left-side sizes must equal half the total length), I only need to binary search over partition positions in the shorter array, checking at each candidate whether the boundary condition holds, and shifting the search range based on which side is violated. I chose binary search over partition points instead of a two-pointer merge because binary search only needs O(log(min(m,n))) candidate partitions, each checked in O(1), giving true logarithmic time — this is a case where a stricter target complexity than O(m+n) is explicitly implied by the problem being labeled Hard and by the fact that a straightforward merge-based approach is the 'obvious but insufficiently optimal' answer here. This runs in O(log(min(m, n))) time, since binary search operates only on the shorter array, and O(1) space, since only a few running index and value variables are tracked regardless of input size."""