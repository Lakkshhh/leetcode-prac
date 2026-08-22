<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">26. Remove Duplicates from Sorted Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Consider the number of <em>unique elements</em> in&nbsp;<code>nums</code> to be <code>k<strong>​​​​​​​</strong></code>​​​​​​​. <meta charset="UTF-8" />After removing duplicates, return the number of unique elements&nbsp;<code>k</code>.</p>

<p><meta charset="UTF-8" />The first&nbsp;<code>k</code>&nbsp;elements of&nbsp;<code>nums</code>&nbsp;should contain the unique numbers in <strong>sorted order</strong>. The remaining elements beyond index&nbsp;<code>k - 1</code>&nbsp;can be ignored.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


# STEP 1 — CLARIFY

**Candidate:** Alright, let me restate this to make sure I've got it. I'm given an integer array `nums` that's already sorted in non-decreasing order. I need to remove duplicates *in-place* so that each unique value appears exactly once, while preserving the relative (sorted) order. I don't return a new array — instead I return an integer `k`, which is the count of unique elements, and the judge only checks that the first `k` slots of `nums` hold the correct unique values in order. Anything past index `k-1` is garbage and doesn't matter.

A few clarifying questions before I dive in:

1. Since the array is guaranteed sorted, duplicates will always be adjacent, right? I don't need to worry about something like `[1, 2, 1]`?
2. The constraint says `1 <= nums.length`, so I don't need to handle an empty array — but should I still defensively code for it, or can I assume length ≥ 1?
3. Can I use extra space — like sorting into a set — or is this explicitly meant to be solved in O(1) extra space given the "in-place" requirement and the custom judge signature?
4. Values range from -100 to 100, so no concerns about overflow or weird types — just plain ints.

**Interviewer:** Good questions. Yes — sorted non-decreasing means duplicates are always adjacent, you won't see `[1,2,1]`. Length is always at least 1, so no empty-array edge case, but no harm being safe. And yes, the in-place / O(1) extra space expectation is real — that's the whole point of the problem, otherwise it's trivial with a set. Go ahead.

---

# STEP 2 — EXEMPLIFY

**Candidate:** Let me pin down two cases.

**Normal case:** `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
Expected: `k = 5`, and the first 5 elements become `[0, 1, 2, 3, 4]`. Reasoning: there are 5 distinct values in the array — 0, 1, 2, 3, 4 — so after de-duping, those are the unique values in sorted order.

**Edge case:** `nums = [1, 1, 1, 1]` — all elements identical.
Expected: `k = 1`, and `nums[0] = 1`. Reasoning: there's only one unique value in the whole array, so after de-duping only a single slot matters.

I'll also mentally flag `nums = [5]` — single element, already trivially unique, `k = 1` — as the true minimal edge case, since the constraints guarantee length ≥ 1.

**Interviewer:** Sounds good. Go ahead to strategy.

---

# STEP 3 — STRATEGIZE (Brute Force)

**Candidate:** The most naive approach I can think of: since I can use some extra space conceptually to reason about it (even if I'd need to copy back), I could build a new list by iterating through `nums` and only appending a value if it's different from the last value I appended — or, even more naively, throw every element into a `set` to dedupe, then sort that set (though it's already sorted, so I could skip the sort), and copy those values back into the front of `nums`.

Even more brute-force than that: for each index `i`, scan every other index `j` to check if `nums[j] == nums[i]` for some `j < i`, and only "keep" `nums[i]` if no earlier duplicate exists. That's the classic quadratic approach that doesn't even exploit the sorted property.

- **Time complexity:** O(n²) for the nested-loop version, or O(n) if I exploit sortedness with a second array/set — but let's call the truly "brute force, ignore all structure" version O(n²) time.
- **Space complexity:** O(n) extra space for the second array/set to hold uniques before copying back.

**Interviewer:** Right, and to be fair the O(n²) version is barely worth dwelling on — it ignores that the array is sorted. What's bothering you about even the O(n) extra-space version, given the problem statement?

---

# STEP 4 — OPTIMIZE

**Candidate:** Right — the issue is the space. The problem explicitly wants in-place modification with (implicitly) O(1) extra space — that's what "in-place" and the judge signature (checking `nums` directly, no return array) are signaling. Building a second array defeats the purpose, even though it's O(n) time.

So the real question: what repeated work or wasted space can I eliminate?

**Interviewer:** Yeah — what's actually redundant here? Think about what "sorted" buys you that an unsorted array wouldn't.

**Candidate:** Because it's sorted, duplicates are always consecutive. So I never need to search for a duplicate — I only ever need to compare an element to its immediate predecessor in the *result* I'm building. That screams **two-pointer / in-place overwrite pattern**: one pointer tracks "the last confirmed-unique slot I've written," and another pointer scans forward through the array looking for the next value that differs from what's at the write pointer.

**Interviewer:** Okay, walk me through the trade-off you're making.

**Candidate:** Sure — I'm trading the O(n) auxiliary space of building a separate deduped array for O(1) space, by reusing the input array itself as both the read buffer and the write buffer. The cost is that I have to be careful never to overwrite a value I haven't read yet — but since my write pointer only ever moves forward at the same pace or slower than my read pointer, I'm guaranteed the write pointer never "laps" or corrupts unread data. So: **trading a second array (extra memory) for careful pointer bookkeeping (extra reasoning, not extra space)** — I still touch every element once, so time stays O(n), but space drops from O(n) to O(1).

Concretely:
- A `write_index` pointer starts at 1 (since `nums[0]` is trivially always kept — first element is always unique so far).
- A `read_index` pointer scans from 1 to the end.
- Whenever `nums[read_index] != nums[write_index - 1]` (i.e., it differs from the last value I've confirmed as unique), I copy `nums[read_index]` into `nums[write_index]` and increment `write_index`.
- At the end, `write_index` *is* `k`.

Expected complexity: **O(n) time** (single pass), **O(1) extra space** (two integer pointers, everything else done in-place).

**Interviewer:** That's the approach I wanted to see. Go ahead and code it up.

---

# STEP 5 — IMPLEMENT

**Candidate:** Here we go, narrating as I write.

```python
def remove_duplicates(nums: list[int]) -> int:
    # Edge case safety: if the array is empty, there are zero uniques.
    # Constraints say length >= 1, but I'll guard anyway.
    if len(nums) == 0:
        return 0

    # write_index tracks the next position in nums where a newly-confirmed
    # unique value should be written. nums[0] is always unique by definition
    # (nothing before it to compare against), so we start writing from index 1.
    write_index = 1

    # read_index scans forward through the array, one element at a time,
    # looking for values that differ from the last value we wrote.
    for read_index in range(1, len(nums)):
        # Compare the current element to the most recently written unique
        # value, which lives at write_index - 1.
        if nums[read_index] != nums[write_index - 1]:
            # It's a new unique value — place it at the write cursor
            # and advance the write cursor by one.
            nums[write_index] = nums[read_index]
            write_index += 1
        # If it's equal, we do nothing — read_index just moves on,
        # effectively skipping this duplicate.

    # write_index now equals the count of unique elements, k.
    return write_index
```

**Time complexity:** O(n) — `read_index` makes a single linear pass over the array; every element is examined exactly once, and each comparison/write is O(1).

**Space complexity:** O(1) — I only allocate two integer variables (`write_index`, `read_index`, the latter coming from the loop itself). No auxiliary array, no recursion stack. The modification happens directly on the input buffer.

**Interviewer:** Looks clean. Let's trace it before we call it done.

---

# STEP 6 — DRY RUN & DEBUG

**Candidate:** Let's trace with the normal case: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`.

```
Initial: nums = [0,0,1,1,1,2,2,3,3,4], write_index = 1

read_index=1: nums[1]=0, compare to nums[write_index-1]=nums[0]=0 -> equal, skip
              write_index still 1

read_index=2: nums[2]=1, compare to nums[0]=0 -> different!
              nums[1] = 1  -> nums = [0,1,1,1,1,2,2,3,3,4]
              write_index = 2

read_index=3: nums[3]=1, compare to nums[write_index-1]=nums[1]=1 -> equal, skip

read_index=4: nums[4]=1, compare to nums[1]=1 -> equal, skip

read_index=5: nums[5]=2, compare to nums[1]=1 -> different!
              nums[2] = 2 -> nums = [0,1,2,1,1,2,2,3,3,4]
              write_index = 3

read_index=6: nums[6]=2, compare to nums[2]=2 -> equal, skip

read_index=7: nums[7]=3, compare to nums[2]=2 -> different!
              nums[3] = 3 -> nums = [0,1,2,3,1,2,2,3,3,4]
              write_index = 4

read_index=8: nums[8]=3, compare to nums[3]=3 -> equal, skip

read_index=9: nums[9]=4, compare to nums[3]=3 -> different!
              nums[4] = 4 -> nums = [0,1,2,3,4,2,2,3,3,4]
              write_index = 5

Loop ends. Return write_index = 5.
```

First 5 elements: `[0, 1, 2, 3, 4]` — matches expected output, and `k = 5` matches too. 

Let me also sanity-check the edge case, `nums = [1, 1, 1, 1]`:

```
Initial: write_index = 1

read_index=1: nums[1]=1, compare nums[0]=1 -> equal, skip
read_index=2: nums[2]=1, compare nums[0]=1 -> equal, skip
read_index=3: nums[3]=1, compare nums[0]=1 -> equal, skip

Return write_index = 1.
```

`k = 1`, `nums[0] = 1` — correct.

No bugs surfaced in this trace — the logic held up on both cases. If I wanted to be extra defensive, I'd double check the single-element array `[5]`: the `for` loop range is `range(1, 1)`, which is empty, so we skip straight to `return write_index`, which is still `1`. Correct — no crash, no off-by-one on the range bound.

**Interviewer:** Nice, no bugs to shake out this round. One thing — walk me back through why you compare against `nums[write_index - 1]` instead of just keeping a separate `last_seen_value` variable?

**Candidate:** Good question — they're functionally equivalent here since `write_index - 1` always points at the last value I actually wrote, so `nums[write_index - 1]` *is* `last_seen_value` by construction. I could introduce a separate variable for slightly more explicit readability — arguably a small clarity win — but it'd be redundant state to keep in sync, and indexing into `nums` directly is just as cheap. I'd call it a style choice, not a correctness or complexity difference.

**Interviewer:** Fair, agreed. That's a wrap — let's talk assessment.

---

# FINAL ASSESSMENT (Interviewer)

**Clarity:** Strong. You restated the problem accurately, asked sharp clarifying questions (especially confirming the sorted-adjacency property and the implicit O(1) space bar), and narrated every step without hand-waving.

**Correctness:** Solution is correct and matches expected output on both the normal case and the all-duplicates edge case, plus you reasoned through the single-element edge case without needing to run it.

**Complexity:** Landed on the optimal O(n) time / O(1) space two-pointer solution, and — importantly — you correctly named the *trade-off* (auxiliary array traded for careful in-place pointer bookkeeping) rather than just naming the pattern. That's exactly the kind of reasoning that separates "I've seen this problem" from "I understand why this works."

**Communication:** Good pacing — you didn't jump to the optimal solution prematurely, you earned it by first stating the brute force and its cost, then let the sorted-property observation drive you to two pointers naturally.

**One thing to tighten up:** In a real onsite, I'd push you a bit harder on *why* the write pointer can never overtake or corrupt the read pointer's unread data — you asserted it but didn't formally justify the invariant. Something like "write_index ≤ read_index always holds, because write_index only increments when we've just read a new unique value at read_index, so it can never advance past the position we're currently reading" would preempt that follow-up before I even ask it.

**Amazon Leadership Principles tie-in:** This problem is a nice small hook for **Frugality** — doing more with less, specifically trading memory for in-place cleverness, which maps directly to "accomplish more with less" in a resource-constrained sense. It also touches **Insist on the Highest Standards**, since the naive O(n) extra-space solution *works* but doesn't meet the implicit bar the problem is setting (in-place, O(1) space) — recognizing and closing that gap without being explicitly told is the kind of standard-raising Amazon likes to hear about in a behavioral story.
