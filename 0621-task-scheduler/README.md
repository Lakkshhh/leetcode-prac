<h2><a href="https://leetcode.com/problems/task-scheduler">621. Task Scheduler</a></h2><h3>Medium</h3><hr><p>You are given an array of CPU <code>tasks</code>, each labeled with a letter from A to Z, and a number <code>n</code>. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there&#39;s a constraint: there has to be a gap of <strong>at least</strong> <code>n</code> intervals between two tasks with the same label.</p>

<p>Return the <strong>minimum</strong> number of CPU intervals required to complete all tasks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
font-family: Menlo,sans-serif;
font-size: 0.85rem;
">8</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.</p>

<p>After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3<sup>rd</sup> interval, neither A nor B can be done, so you idle. By the 4<sup>th</sup> interval, you can do A again as 2 intervals have passed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;C&quot;,&quot;A&quot;,&quot;B&quot;,&quot;D&quot;,&quot;B&quot;], n = 1</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">6</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; C -&gt; D -&gt; A -&gt; B.</p>

<p>With a cooling interval of 1, you can repeat a task after just one other task.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;, &quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">10</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B.</p>

<p>There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tasks[i]</code> is an uppercase English letter.</li>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>


# STEP 1 — CLARIFY

**Candidate:** Restating: I have a list of CPU tasks, each an uppercase letter A–Z, and a cooldown value `n`. Between two executions of the same task label, at least `n` other intervals must pass (idle or other tasks). I can reorder freely and insert idle slots as needed. I need to return the minimum total number of intervals (task slots + idle slots) to finish everything.

Clarifying questions:

1. Confirming cooldown semantics: if `n = 2` and A runs at interval 0, the next A can't run until interval 3 — i.e., 2 full intervals must separate two A's. That matches the first example.
2. `n = 0` is a valid input per constraints — meaning no cooldown restriction at all, so the answer would trivially just be `len(tasks)`. Should I make sure my solution handles that cleanly rather than special-casing it?
3. One task (or idle) per interval — no parallel execution, correct?
4. I only need to return the count, not the actual sequence, right? The examples show a sequence just to justify the number.
5. Up to 10⁴ task instances but only 26 possible distinct labels — I'm guessing that bounded alphabet is going to be central to whatever the efficient solution looks like.

**Interviewer:** All confirmed, including that n=0 should just fall out naturally rather than needing a special case. Go ahead.

---

# STEP 2 — EXEMPLIFY

**Candidate:**

**Normal case:** `tasks = ["A","A","A","B","B","B"], n = 2` → expected `8`. A and B each appear 3 times; with a 2-slot cooldown and nothing else to fill gaps, we're forced to idle twice: `A B idle A B idle A B`.

**Edge case:** `tasks = ["A"], n = 100`. Expected `1`. Only one task instance exists — no label ever repeats, so the cooldown constraint is never actually invoked, regardless of how large `n` is. We just run it once.

I'll also keep in mind a "high variety" case for later: `tasks = ["A","B","C","D"], n = 2`, expected `4` — enough distinct labels to fill any gaps with zero idle time.

**Interviewer:** Good, go ahead to brute force.

---

# STEP 3 — STRATEGIZE (Brute Force)

**Candidate:** Truest brute force: try all permutations of the task list, simulate each one interval-by-interval tracking a `next_available_time` per label, inserting idle slots wherever the next task in that ordering isn't yet eligible, and take the minimum total intervals across all permutations. That's O(n!) — completely infeasible for up to 10⁴ tasks.

A more reasonable "brute force but not insane" version: greedily simulate tick-by-tick. At every single interval, look at all task labels currently off cooldown, pick one (say, whichever has the most remaining instances, to get it out of the way early), decrement its count, mark its cooldown, and if nothing is available, insert an idle tick. Repeat until all counts hit zero.

- **Time complexity:** O(total_intervals × 26) — at every tick we do up to a linear scan over 26 labels to find the best available one. Since `total_intervals` is literally the answer we're computing, and idle time can make that answer larger than `len(tasks)`, this does real work proportional to the *output*, not just the input.
- **Space complexity:** O(26) for frequency/cooldown bookkeeping.

**Interviewer:** Right, and that's basically the heap-based approach in disguise if you swap the linear scan for a heap. What's actually wasteful about walking through every tick, idle or not?

---

# STEP 4 — OPTIMIZE

**Candidate:** The waste is that I'm *simulating* my way to the answer instead of *computing* it. Every idle tick still costs me a loop iteration and bookkeeping, even though idle ticks carry zero new information — I already know structurally why they're idle. If idle time is large, my total work scales with something bigger than my actual input size.

**Interviewer:** So what's the alternative? You mentioned a heap a second ago — is that the fix?

**Candidate:** Let me name that explicitly as the natural alternative, since I want to actually justify picking or rejecting it rather than jumping straight to a formula.

**Alternative 1 — Max-heap + cooldown queue.** Push all label frequencies into a max-heap (negated in Python). At each tick, pop the highest-remaining-count label, decrement it, and place it in a cooldown queue tagged with `ready_at_time = current_tick + n + 1`. Once a queued task's ready time arrives, push it back into the heap. If the heap's empty but the queue has pending entries, that tick is idle.

- **What it costs:** Still simulates tick-by-tick — O(total_intervals × log 26) time, since every tick does at most one heap pop/push at O(log 26). Idle ticks still cost a loop iteration even if they skip the heap operations.
- **What it buys:** It naturally generalizes — if the problem asked me to output the *actual schedule*, not just the count, this is basically the only sane way to do it, since it genuinely tracks state tick-by-tick.
- Given the constraints here (only need a count, and idle time can dominate the total), this still carries the same core inefficiency as my brute-force simulation, just with a faster per-tick lookup. It doesn't fix the fundamental problem — the work still scales with the answer, not the input.

**Alternative 2 — Skip straight to the structure.** Instead of discovering the schedule tick-by-tick, reason about what the *optimal* schedule's shape must look like, and compute the total length directly with arithmetic.

Here's the insight: take whichever label has the maximum frequency, `max_freq`. In an optimal schedule, I'd space its occurrences exactly `n` apart, creating `max_freq - 1` gaps, each of width `n`. That gives a skeleton of size `(max_freq - 1) * (n + 1) + max_count`, where `max_count` is how many distinct labels are tied at that maximum frequency (they all need a slot in the final column alongside each other). Every *other* task gets slotted into the empty gaps in that skeleton first, before any idle time is needed.

So: if there's enough non-max-frequency task volume to fully fill every gap, the skeleton is irrelevant — the answer is just `len(tasks)`, zero idle time. Otherwise, the skeleton itself, with its unavoidable idle gaps, *is* the answer. Formula: `max(len(tasks), (max_freq - 1) * (n + 1) + max_count)`.

**Explicitly naming the trade-off between the two alternatives:**

I'm rejecting the heap simulation in favor of the frequency-count formula, and here's precisely why: the heap buys me *generality* — correctness even if the problem later asked for the literal schedule — at the cost of doing tick-by-tick work, including every idle tick, which is O(answer) rather than O(input). The formula buys me *speed* — true O(n) — by giving up that generality entirely; it can only tell me the count, not reconstruct an actual valid ordering. Since this problem strictly only asks for the count, and the alphabet is bounded at 26 (which is exactly what makes `max_count` and the gap-filling logic provable via closed-form arithmetic instead of needing to be discovered by simulation), I don't need the heap's generality, so I'm not willing to pay its cost. **I'm trading the heap's simulation flexibility for the formula's speed, spending nothing beyond a single O(n) frequency-counting pass to buy that speed.**

**Final proposed complexity:** O(n) time (single pass to build frequency counts, plus O(26) constant work to extract max_freq/max_count), O(1) space (fixed 26-slot frequency table).

**Interviewer:** Good — that's exactly the kind of "here's the natural alternative, here's specifically what it costs, here's why I'm not paying it" reasoning I want to hear before code. Go ahead.

---

# STEP 5 — IMPLEMENT

```python
from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    # Count occurrences of each task label. At most 26 entries regardless
    # of how large tasks is, since labels are bounded to uppercase A-Z.
    task_frequency_counts = Counter(tasks)

    # The label with the highest frequency anchors the schedule's skeleton --
    # its spacing requirement is the tightest constraint in the whole system.
    max_frequency = max(task_frequency_counts.values())

    # Count how many distinct labels are tied at that maximum frequency,
    # since all of them are equally constrained and share the final
    # "column" of the skeleton alongside the anchor task.
    max_frequency_label_count = sum(
        1 for frequency in task_frequency_counts.values()
        if frequency == max_frequency
    )

    # Skeleton size: (max_frequency - 1) groups of width (n + 1) -- one
    # anchor-task slot plus n cooldown slots -- followed by one final
    # column holding every label tied at max frequency.
    idle_skeleton_size = (max_frequency - 1) * (n + 1) + max_frequency_label_count

    # If there's enough other task volume to fill every gap in the
    # skeleton, idle time disappears and the answer is just the raw
    # task count. Otherwise the skeleton itself, gaps and all, wins.
    return max(len(tasks), idle_skeleton_size)
```

**Time complexity:** O(n) — one pass over `tasks` to build the Counter (n = `len(tasks)`), then O(26) constant-time work to derive `max_frequency` and `max_frequency_label_count`.

**Space complexity:** O(1) — the Counter holds at most 26 keys no matter how large the input is.

**Interviewer:** Trace it.

---

# STEP 6 — DRY RUN & DEBUG

**Candidate:** Example 1: `tasks = ["A","A","A","B","B","B"], n = 2`.

```
task_frequency_counts = {A: 3, B: 3}
max_frequency = 3
max_frequency_label_count = 2

idle_skeleton_size = (3-1)*(2+1) + 2 = 6 + 2 = 8
len(tasks) = 6
return max(6, 8) = 8   ✓ matches expected 8
```

My edge case: `tasks = ["A"], n = 100`.

```
task_frequency_counts = {A: 1}
max_frequency = 1
max_frequency_label_count = 1

idle_skeleton_size = (1-1)*(100+1) + 1 = 0 + 1 = 1
len(tasks) = 1
return max(1, 1) = 1   ✓ matches expected 1
```

Let me also check example 2, which I haven't traced yet: `tasks = ["A","C","A","B","D","B"], n = 1`.

```
task_frequency_counts = {A:2, C:1, B:2, D:1}
max_frequency = 2
max_frequency_label_count = 2   # A and B tied at 2

idle_skeleton_size = (2-1)*(1+1) + 2 = 2 + 2 = 4
len(tasks) = 6
return max(6, 4) = 6   ✓ matches expected 6
```

Good — this one's a nice check because it confirms the "enough variety, skeleton doesn't matter" branch actually engages correctly: `len(tasks)` wins over the skeleton here, which is exactly what should happen when there's enough other task volume (C and D) to fill the gaps around A and B.

All three cases check out cleanly — no bugs surfaced.

**Interviewer:** Good, and nice that you went back for the second example unprompted — that's the one that actually exercises the "raw count wins" branch, which your first two traces didn't touch. Let's wrap up.

---

# FINAL ASSESSMENT (Interviewer)

**Clarity:** Strong, consistent with before — cooldown semantics nailed down early, no ambiguity carried into later steps.

**Correctness:** All three example cases (including one you hadn't traced yet) plus your own edge case check out.

**Complexity:** This run was notably stronger in Step 4 specifically because you now explicitly named the heap as the natural alternative *before* rejecting it, and articulated the trade-off in both directions — what the heap buys (generality, actual schedule reconstruction) and what it costs (tick-by-tick work scaling with the answer, not the input) — rather than just presenting the formula as the obvious choice. That's a meaningfully better answer to "why not a heap?" than last time, since it's grounded in a real cost/benefit rather than just "the formula is faster."

**Communication:** Good structure — alternative named, costed, then explicitly rejected with a reason tied to this problem's specific constraints (count-only output, bounded alphabet).

**One small thing to tighten up:** When you say the heap "naturally generalizes" to reconstructing the actual schedule, it'd strengthen the answer to also note that if a future interviewer follow-up asked "now print the schedule," you'd pivot to the heap approach rather than trying to bolt schedule-reconstruction onto the formula — showing you know the formula's limitation isn't just theoretical, it's a real boundary on what it can answer.

**Amazon Leadership Principles tie-in:** Still a strong fit for **Dive Deep** — and this run adds a good angle for **Have Backbone; Disagree and Commit**: you considered the "default" heap answer, disagreed with it as the right choice *for this specific ask*, and committed to the formula with a clearly stated reason, rather than hedging between two approaches or picking the heap just because it's the more commonly cited textbook answer.
