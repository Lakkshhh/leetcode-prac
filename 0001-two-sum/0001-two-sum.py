class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}  # value -> index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in value_to_index:
                return [value_to_index[complement], index]
            value_to_index[num] = index


"""The brute-force way to find two numbers summing to target is to check every pair, but that means for each number I'm re-scanning the rest of the array to find its complement, which is wasted repeated work — so instead, as I walk through the array once, I ask 'have I already seen the number that would complete this pair?' before I even look ahead, which flips the problem from 'search for a partner' into 'remember what I've seen and do an O(1) lookup.' I use a hash map from value to index because I need both fast membership checking and the original index to return, and a plain set would tell me a complement exists but not where. I chose this single-pass hash map over a two-pass version (build the whole map first, then scan for complements) because the single-pass version naturally avoids matching a number with itself before it's been seen, and it's no more complex to write while doing strictly less redundant work. This runs in O(n) time, since each element is processed once with O(1) average-case hash map operations, and O(n) space for the hash map in the worst case where no match is found until the very end."""