class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern_to_words = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for letter_index in range(len(word)):
                pattern = word[:letter_index] + "*" + word[letter_index + 1:]
                pattern_to_words[pattern].append(word)

        visited_words = set([beginWord])
        word_queue = deque([beginWord])
        transformation_length = 1
        while word_queue:
            for i in range(len(word_queue)):
                word = word_queue.popleft()
                if word == endWord:
                    return transformation_length
                for letter_index in range(len(word)):
                    pattern = word[:letter_index] + "*" + word[letter_index + 1:]
                    for neighbor_word in pattern_to_words[pattern]:
                        if neighbor_word not in visited_words:
                            visited_words.add(neighbor_word)
                            word_queue.append(neighbor_word)
            transformation_length += 1
        return 0


"""Since I need the shortest transformation sequence and every transformation step has equal 'cost' (one letter swap), this is unweighted shortest-path territory, which means BFS, expanding level by level exactly like Rotting Oranges — each full wave through the queue represents one additional word in the sequence. The tricky part is that words aren't explicitly connected — I don't have a graph handed to me — so I need to build adjacency myself, and comparing every word against every other word directly would be expensive; instead I generate wildcard patterns for each word (swapping one letter at a time for *), and group all words sharing a pattern together, since any two words sharing a pattern differ by exactly that one letter, which turns 'find all one-letter-different neighbors' into a cheap dictionary lookup instead of a pairwise comparison. I chose this wildcard-pattern hashmap over directly comparing every pair of words because pairwise comparison is O(wordCount² · wordLength), whereas the pattern-bucketing approach is O(wordCount · wordLength²) to build, and I chose BFS over DFS because DFS would find a path but not guarantee it's the shortest one without extra bookkeeping, whereas BFS's level-by-level expansion guarantees the first time I reach endWord it's via the shortest possible sequence. This runs in O(wordCount · wordLength²) time, since building the pattern map takes wordLength work per word to generate patterns and BFS visits each word once, doing wordLength work per word to regenerate its patterns during traversal, and O(wordCount · wordLength) space for storing the pattern-to-words map and the visited set."""