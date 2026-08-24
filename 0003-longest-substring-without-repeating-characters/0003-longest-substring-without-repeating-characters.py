class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_in_window = set()
        left_pointer = 0
        max_length = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in chars_in_window:
                chars_in_window.remove(s[left_pointer])
                left_pointer += 1
            chars_in_window.add(s[right_pointer])
            max_length = max(max_length, right_pointer - left_pointer + 1)
        return max_length


"""Checking every possible substring for duplicate characters would mean re-scanning overlapping ranges repeatedly, which is wasted work — since I only care about contiguous runs, I can instead grow a window from the right and only shrink it from the left when a duplicate shows up, never restarting from scratch, which is the sliding window trigger. I maintain a set of characters currently inside the window; when the character at the right pointer is already in that set, I shrink from the left — removing characters and advancing the left pointer — until the duplicate is gone, then add the new character and record the window size if it's the largest seen so far. I chose a set over a hash map here because I only need fast membership checks ('is this character already in my window'), not any associated value like an index — a map would be necessary if I wanted to jump the left pointer directly to the duplicate's position instead of shrinking one step at a time, which is a valid and slightly faster-in-practice alternative I considered, but the set-based version is simpler to reason about and both share the same asymptotic bound. This runs in O(n) time, since each character is added and removed from the window at most once across the entire traversal despite the nested while loop, and O(min(n, charset_size)) space for the set, bounded by whichever is smaller — the string length or the size of the possible character set."""