from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            letter_frequency = [0] * 26
            for char in word:
                letter_frequency[ord(char) - ord('a')] += 1
            anagram_groups[tuple(letter_frequency)].append(word)
        return list(anagram_groups.values())


"""Two strings are anagrams exactly when they share the same multiset of letters, so I need a canonical key that's identical for every anagram of a word but different for non-anagrams — the two natural candidates are sorting each string's characters (so anagrams collapse to the same sorted string) or building a fixed-size letter-frequency count (so anagrams collapse to the same count array), and I'll group words into a hash map keyed by whichever canonical form I pick. I chose the frequency-count array over sorting because sorting each string costs O(k log k) per word, while building a 26-slot frequency count costs only O(k), and since the alphabet is fixed and small (lowercase a-z), a frequency array is a cheap, bounded-size key rather than relying on comparison-based sorting; I convert it to a tuple specifically because Python lists aren't hashable and can't be used directly as dictionary keys, whereas tuples are. This runs in O(n · k) time, where n is the number of strings and k is the average string length, since each string requires one O(k) pass to build its frequency key, and O(n · k) space in the worst case to store all the words across all the groups plus their keys."""