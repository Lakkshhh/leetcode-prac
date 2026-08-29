class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combinations = []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current_combination):
            if len(current_combination) == len(digits):
                combinations.append(current_combination)
                return
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, current_combination + letter)

        if digits:
            backtrack(0, "")
        return combinations


"""Let me first make sure I understand the problem: I'm given a string of digits from two through nine, like a phone keypad, and I need to return every possible letter combination those digits could represent, where each digit maps to a fixed set of letters. The key observation is that this is really about building up combinations one digit at a time, and at each digit I have a small fixed set of choices, so I need to explore every possible path through those choices, which immediately makes me think of backtracking rather than trying to construct everything iteratively. So I think a good way to represent the digit-to-letter mapping is just a hash map, since it gives me constant time lookup for which letters correspond to whichever digit I'm currently on. From there, I write a recursive helper that tracks which digit index I'm currently building on and the combination string I've built so far, and the base case is when that combination's length matches the total number of digits, meaning I've picked one letter for every digit, so I add it to my results and return. Otherwise, I look up all the letters for the current digit, and for each one, I recurse forward to the next digit index with that letter appended to my current combination, which naturally explores every branch since after each recursive call returns, the loop just moves on to try the next letter option at that same position. One edge case I'd call out is handling the empty input string up front, since if there are no digits at all, there are no combinations to build, so I just return an empty list without ever starting the recursion. In terms of complexity, if there are n digits, and digits like 7 and 9 map to four letters instead of three, the time complexity is O(4^n times n) in the worst case, since there are up to four choices per digit, and building each combination string takes O(n) work, and the space complexity is O(n) for the recursion depth aside from the output itself, since the call stack only ever goes as deep as the number of digits.

Since each digit maps to multiple possible letters and I need every combination across all digit positions, this is a classic backtracking/combinatorial-generation trigger — at each position I have several choices, and I need to explore all of them, building up a partial combination one letter at a time and only recording it once it's complete. I recurse through digit positions left to right, and at each position I loop over that digit's possible letters, appending one letter and recursing deeper; when the current combination's length matches the total number of digits, that's a complete combination and I record it. I chose backtracking (recursive exploration with implicit backtracking via string concatenation, rather than in-place mutation and undo) over an iterative approach that builds up the full combination list layer-by-layer via repeated list expansion, because backtracking makes the choice-and-recurse structure explicit and easy to reason about, though the iterative layer-by-layer expansion is a valid, equally-correct alternative that avoids recursion depth concerns for very long digit strings. This runs in O(4^n · n) time in the worst case, where n is the number of digits, since digits like 7 and 9 map to 4 letters each, there are up to 4^n total combinations, and building each one costs O(n) due to string concatenation, and O(n) space for the recursion depth, excluding the space needed to store the output itself."""