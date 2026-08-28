class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = vote_count = 0

        for num in nums:
            if vote_count == 0:
                candidate = num
            vote_count += (1 if num == candidate else -1)
        return candidate

    # Hashmap solution
    # count = defaultdict(int)
    #     res = maxCount = 0

    #     for num in nums:
    #         count[num] += 1
    #         if maxCount < count[num]:
    #             res = num
    #             maxCount = count[num]
    #     return res


"""Let me first make sure I understand the problem: I'm given an array of numbers and I need to find the majority element, meaning the value that appears more than n/2 times, and I can assume that such an element always exists. The key observation is that since the majority element occurs more than half the time, if I imagine every occurrence of it as a "plus one" vote and every other number as a "minus one" vote, the total sum across the whole array has to end up positive, because the majority element alone outweighs everything else combined. That makes me think I don't actually need any extra data structure like a hash map to count frequencies — I can just track a running candidate and a running vote count as I scan through once. So the approach is: I keep a candidate and a counter starting at zero, and as I go through each number, if my counter ever drops to zero, I treat that as a signal that I have no strong candidate right now, so I pick the current number as the new candidate; then I bump the counter up if the current number matches my candidate, or down if it doesn't. The intuition behind why this works is that non-majority numbers effectively cancel each other out against the candidate, but since the majority element outnumbers everything else combined, it always survives as the leftover candidate by the end. One thing I'd mention is that this approach relies on the guarantee that a majority element exists — if it didn't, this would just return some element without actually verifying it's the majority, so in a follow-up I'd want to do a second pass to confirm the count if that guarantee wasn't given. In terms of complexity, this is O(n) time since it's a single pass through the array, and O(1) space since I'm only tracking a candidate and a counter, no matter how large the input is.

A hash map frequency count would work straightforwardly — tally every element's count and return whichever exceeds n/2 — but the 'more than half' guarantee is a strong enough constraint that it enables something cheaper: the Boyer-Moore voting trick, where I treat each element as either supporting or opposing a current candidate, incrementing a vote count when I see the candidate again and decrementing otherwise; whenever the vote count hits zero, I discard the current candidate and adopt whatever element comes next. This works specifically because the majority element appears more than half the time — any equal number of 'votes against' from all other elements combined can never fully cancel out the majority element's surplus, so whichever candidate survives to the end must be it. I chose Boyer-Moore voting over the hash map approach because it achieves O(1) space instead of O(n), trading away the ability to report actual frequency counts (which I don't need here) for a much leaner memory footprint — this is a case where the problem's specific guarantee (a true majority exists) unlocks a cheaper structure than the fully general 'find the most frequent element' version would allow. This runs in O(n) time, since the array is scanned exactly once, and O(1) space, since only two running variables are tracked regardless of input size."""