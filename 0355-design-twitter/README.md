<h2><a href="https://leetcode.com/problems/design-twitter">355. Design Twitter</a></h2><h3>Medium</h3><hr><p>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user&#39;s news feed.</p>

<p>Implement the <code>Twitter</code> class:</p>

<ul>
	<li><code>Twitter()</code> Initializes your twitter object.</li>
	<li><code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.</li>
	<li><code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user&#39;s news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be <strong>ordered from most recent to least recent</strong>.</li>
	<li><code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.</li>
	<li><code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Twitter&quot;, &quot;postTweet&quot;, &quot;getNewsFeed&quot;, &quot;follow&quot;, &quot;postTweet&quot;, &quot;getNewsFeed&quot;, &quot;unfollow&quot;, &quot;getNewsFeed&quot;]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
<strong>Output</strong>
[null, null, [5], null, null, [6, 5], null, [5]]

<strong>Explanation</strong>
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 1 tweet id -&gt; [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 2 tweet ids -&gt; [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1&#39;s news feed should return a list with 1 tweet id -&gt; [5], since user 1 is no longer following user 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId, followerId, followeeId &lt;= 500</code></li>
	<li><code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code></li>
	<li>All the tweets have <strong>unique</strong> IDs.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>postTweet</code>, <code>getNewsFeed</code>, <code>follow</code>, and <code>unfollow</code>.</li>
	<li>A user cannot follow himself.</li>
</ul>


# STEP 1 — CLARIFY

**Candidate:** Let me restate this. I'm designing a simplified Twitter with four operations:

- `postTweet(userId, tweetId)` — user posts a tweet, and I'm told each `tweetId` passed in is globally unique, so I don't need to worry about collisions.
- `getNewsFeed(userId)` — return up to the 10 most recent tweet IDs visible to this user, where "visible" means posted by the user themself or by anyone they follow, ordered newest-first.
- `follow(followerId, followeeId)` — followerId starts following followeeId.
- `unfollow(followerId, followeeId)` — the reverse.

Some clarifying questions:

1. "Most recent" — I'm assuming this means recency is determined by *post order*, not by tweetId value directly, although since tweetIds are unique and presumably assigned in increasing order as posts happen, I could actually use a global increasing counter/timestamp at post time rather than relying on tweetId ordering. Is that a safe assumption — that I should track my own timestamp rather than assume tweetId is monotonic?
2. If `getNewsFeed` is called for a user who has posted fewer than 10 tweets total combined with followees, do I just return everything available, sorted? Presumably yes.
3. Can a user follow someone who's never posted, or call `getNewsFeed` for a user who doesn't exist yet / has never posted or followed anyone? Should that just return an empty list rather than erroring?
4. Is `follow` idempotent — if I call `follow(1,2)` twice, should that be a no-op the second time, or could it double-count? And is `unfollow` safe to call even if not currently following?
5. Given the constraints — up to 500 users, up to 3×10⁴ total operations across all four methods, tweetIds up to 10⁴ — this tells me `getNewsFeed` needs to be efficient since it could be called tens of thousands of times, potentially against a user following many others.

**Interviewer:** Good instincts. Yes — use your own internal timestamp/counter at post time, don't trust tweetId to be chronological. Return whatever's available if fewer than 10 exist. Non-existent or inactive users just get empty feeds, no errors. Follow/unfollow should behave sanely — double-follow is a no-op, unfollow-when-not-following is a no-op. And yes, `getNewsFeed` is going to be your hot path — assume it's called a lot. Go ahead.

---

# STEP 2 — EXEMPLIFY

**Candidate:** Let me build on the given example, plus think of an edge case of my own.

**Normal case (essentially the prompt's example):**
- `postTweet(1, 5)` → user 1 has tweet 5.
- `getNewsFeed(1)` → `[5]` (only their own tweet so far).
- `follow(1, 2)` → user 1 now follows user 2.
- `postTweet(2, 6)` → user 2 posts tweet 6, which happens *after* tweet 5 chronologically.
- `getNewsFeed(1)` → `[6, 5]` — newest first, and since user 1 follows user 2, both tweets are visible.
- `unfollow(1, 2)` → user 1 no longer follows user 2.
- `getNewsFeed(1)` → `[5]` — user 2's tweet 6 disappears from the feed even though it still "exists," because visibility is follow-relationship-dependent at query time, not baked in at post time.

**Edge case:** A user who follows nobody and has never posted calls `getNewsFeed`.
- `getNewsFeed(3)` where user 3 has done nothing yet → expected `[]`, empty list. There's no data to show, and it shouldn't error just because user 3 has never explicitly been "created" — since there's no explicit `createUser` method, any userId should just work lazily.

I'll also mentally flag a "more than 10 tweets" edge case: if user 1 follows user 2, and user 2 alone has posted 15 tweets, `getNewsFeed(1)` should return only the 10 most recent of those 15, not all 15.

**Interviewer:** Good, that last one is exactly the kind of case I'd want you to think about before coding. Go ahead to brute force.

---

# STEP 3 — STRATEGIZE (Brute Force)

**Candidate:** Naive approach:

- Maintain a global list of *all* tweets ever posted, each stored as `(timestamp, userId, tweetId)`.
- Maintain a `followMap`: `userId -> set of followeeIds` they follow.
- For `postTweet`: just append `(timestamp, userId, tweetId)` to the global list, increment a global timestamp counter.
- For `follow`/`unfollow`: add/remove from the `followMap` set.
- For `getNewsFeed(userId)`: scan the *entire* global tweet list, filter down to tweets where the poster is either `userId` itself or in `followMap[userId]`, sort the filtered results by timestamp descending, and take the top 10.

**Time complexity:**
- `postTweet`: O(1) — just an append.
- `follow`/`unfollow`: O(1) — set insert/remove.
- `getNewsFeed`: O(T log T) where T is the *total number of tweets ever posted across all users* — because I'm filtering and sorting the entire global list every single call, regardless of how many tweets are actually relevant to this user.

**Space complexity:** O(T + U) — T for all tweets stored globally, U for the follow relationships.

**Interviewer:** Okay — that `getNewsFeed` cost is going to sting given the constraints. What's the actual problem with scanning the whole global list every time?

---

# STEP 4 — OPTIMIZE

**Candidate:** Right — the issue is that `getNewsFeed` re-scans and re-sorts *every tweet that has ever existed in the system*, even tweets from users totally unrelated to the querying user, every single time it's called. With up to 3×10⁴ operations, if a meaningful fraction of those are `getNewsFeed` calls late in the sequence when the global tweet list is large, that's a lot of wasted work re-examining irrelevant data repeatedly.

**Interviewer:** So what's actually relevant to a given `getNewsFeed(userId)` call? You don't need *all* tweets — what do you need?

**Candidate:** I only need tweets from the small set of people `userId` follows (plus themself) — not the entire universe of tweets. So the first improvement: instead of one global tweet list, store **per-user tweet lists** — `userTweets[userId] -> list of (timestamp, tweetId)` for tweets *that specific user posted*. That way `postTweet` is still O(1) (append to that user's own list), and `getNewsFeed` only has to look at the lists belonging to `userId` and their followees — a much smaller candidate set — rather than the whole system.

**Interviewer:** Okay, that narrows the candidate set. But each of those followee lists could still be long individually if someone's a prolific poster. You only ever need the top 10 *merged* across however many followees there are — what does that smell like?

**Candidate:** That's a classic **merge k sorted lists** problem — each followee's tweet list is already sorted by timestamp (since I append in chronological order, so it's naturally non-decreasing/increasing). I need the top 10 *merged* by timestamp across up to `k` lists, where `k` is the number of people followed (bounded by ~500 users). The classic efficient pattern for merging k sorted lists and pulling off the top elements is a **heap** — specifically, I can do a bounded merge using a max-heap (or in Python, a min-heap with negated timestamps) seeded with just the *most recent* tweet from each relevant user's list, then repeatedly pop the global max and push that same user's next-most-recent tweet, stopping after I've pulled 10 total.

**Interviewer:** Name the trade-off.

**Candidate:** Sure — I'm trading the brute-force approach's "sort everything, every time" cost for a heap-based merge that only ever touches **at most `k` initial entries (one per followee/self) plus up to 10 pop-and-replace steps**, rather than the full length of every user's tweet history. So specifically: I'm trading a full sort of all relevant tweets — O(m log m) where m is total relevant tweet count — for a **bounded k-way merge** costing roughly O(k + 10 log k), since the heap only ever holds at most `k` elements at a time and I only extract 10 elements. I'm spending a bit of extra bookkeeping complexity (tracking each followee's read-cursor into their tweet list) to save the cost of sorting or scanning full histories on every single call. Essentially: **trading "recompute everything from scratch every query" for "only ever look at the frontier of each relevant user's timeline."**

Also, for `follow`/`unfollow`, I'll use a `dict[userId] -> set[followeeId]` for O(1) average add/remove/lookup, and I should make sure a user always implicitly "follows themself" for feed purposes — I'll handle that by just always including `userId` itself alongside their followee set at query time, rather than literally inserting a self-follow edge (cleaner, avoids weird edge cases if someone explicitly tries to follow/unfollow themselves, though the constraints say that won't happen anyway).

**Final proposed complexity:**
- `postTweet`: O(1)
- `follow` / `unfollow`: O(1) average
- `getNewsFeed`: O(k log k) where k = number of people followed by the querying user (each heap push/pop is O(log k), and we do at most k initial pushes + 10 pop/push cycles) — much better than O(T log T) over the whole system, and bounded by the small "k ≤ 500 users" constraint rather than by total tweet volume, which can be up to 3×10⁴.

**Interviewer:** That's the approach I was hoping you'd land on. Let's see the code.

---

# STEP 5 — IMPLEMENT

**Candidate:** Let me build this out piece by piece, narrating as I go.

```python
import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        # Global counter acting as a logical timestamp. Incremented on every
        # postTweet call so we always know relative posting order, without
        # trusting tweetId to be chronological.
        self.timestamp_counter = 0

        # Maps userId -> list of (timestamp, tweetId) tuples, in the order
        # they were posted (so naturally increasing by timestamp).
        # Using a plain list; appends are O(1) amortized.
        self.user_tweets = defaultdict(list)

        # Maps followerId -> set of followeeIds they follow.
        # A set gives O(1) average add/remove/membership-check.
        self.user_following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Record this tweet under the posting user's own timeline,
        # tagged with the current global timestamp, then advance the clock.
        self.user_tweets[userId].append((self.timestamp_counter, tweetId))
        self.timestamp_counter += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to follower's following-set. Using a set means
        # calling follow twice on the same pair is naturally idempotent.
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard() rather than remove() so this is a safe no-op
        # if followerId wasn't following followeeId in the first place.
        self.user_following[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> list[int]:
        # Build the set of relevant posters: the user themself, plus
        # everyone they follow. Using a set union so self-follow duplication
        # isn't an issue even if userId happens to already be "following" itself.
        relevant_users = self.user_following[userId] | {userId}

        # This max-heap (simulated via negated timestamps, since Python's
        # heapq is a min-heap) will hold, at any point, one "frontier" entry
        # per relevant user: their most recent not-yet-emitted tweet.
        # Each heap entry is (negated_timestamp, tweetId, ownerUserId, indexIntoTheirList).
        max_heap = []

        for candidate_user_id in relevant_users:
            user_tweet_list = self.user_tweets[candidate_user_id]
            if user_tweet_list:
                # Their most recent tweet is at the end of the list
                # since we append in chronological order.
                last_index = len(user_tweet_list) - 1
                tweet_timestamp, tweet_id = user_tweet_list[last_index]
                # Negate timestamp so the "largest" (most recent) timestamp
                # becomes the smallest value, which heapq will pop first.
                heapq.heappush(
                    max_heap,
                    (-tweet_timestamp, tweet_id, candidate_user_id, last_index)
                )

        recent_tweet_ids = []

        # Pull up to 10 tweets, always taking the globally most recent
        # available tweet across all relevant users' frontiers.
        while max_heap and len(recent_tweet_ids) < 10:
            negated_timestamp, tweet_id, owner_user_id, tweet_index = heapq.heappop(max_heap)
            recent_tweet_ids.append(tweet_id)

            # After consuming this user's most recent tweet, push their
            # *next* most recent tweet (the one just before it in their list),
            # if one exists, so it becomes available for future pops.
            next_index = tweet_index - 1
            if next_index >= 0:
                next_timestamp, next_tweet_id = self.user_tweets[owner_user_id][next_index]
                heapq.heappush(
                    max_heap,
                    (-next_timestamp, next_tweet_id, owner_user_id, next_index)
                )

        return recent_tweet_ids
```

**Time complexity:**
- `postTweet`: O(1) amortized (list append).
- `follow` / `unfollow`: O(1) average (set operations).
- `getNewsFeed`: Let `k` = number of relevant users (followees + self, bounded by ~500). Building the initial heap is O(k log k) (k pushes, each O(log k)). The extraction loop runs at most 10 times, each doing one pop and at most one push, both O(log k). So total is O(k log k) — dominated by the initial heap construction, not by total tweet volume across the whole system. That's the win over the brute force's O(T log T).

**Space complexity:** O(U + T) overall for storing all tweets and follow relationships across the system (`U` = users, `T` = total tweets), plus O(k) transient space for the heap during a single `getNewsFeed` call.

**Interviewer:** Reasonable. Let's trace it.

---

# STEP 6 — DRY RUN & DEBUG

**Candidate:** Let's trace through the exact sequence from the prompt's example.

```
Twitter() 
  timestamp_counter = 0
  user_tweets = {}
  user_following = {}

postTweet(1, 5)
  user_tweets[1] = [(0, 5)]
  timestamp_counter = 1

getNewsFeed(1)
  relevant_users = user_following[1] | {1} = {} | {1} = {1}
  For user 1: user_tweets[1] = [(0,5)], last_index=0, push (-0, 5, 1, 0)
  max_heap = [(0, 5, 1, 0)]   # note -0 == 0
  
  Pop (0, 5, 1, 0) -> recent_tweet_ids = [5]
    next_index = -1 -> nothing to push
  Heap empty, loop ends.
  
  Return [5]  ✓ matches expected [5]

follow(1, 2)
  user_following[1] = {2}

postTweet(2, 6)
  user_tweets[2] = [(1, 6)]
  timestamp_counter = 2

getNewsFeed(1)
  relevant_users = {2} | {1} = {1, 2}
  
  For user 1: user_tweets[1] = [(0,5)], last_index=0, push (-0, 5, 1, 0)
  For user 2: user_tweets[2] = [(1,6)], last_index=0, push (-1, 6, 2, 0)
  max_heap after pushes (as a min-heap on first element): 
    entries: (0, 5, 1, 0) and (-1, 6, 2, 0)
    Since -1 < 0, heapq will pop (-1, 6, 2, 0) first — correct,
    because timestamp 1 (tweet 6) is more recent than timestamp 0 (tweet 5).
  
  Pop (-1, 6, 2, 0) -> recent_tweet_ids = [6]
    next_index = -1 -> nothing to push for user 2
  Pop (0, 5, 1, 0) -> recent_tweet_ids = [6, 5]
    next_index = -1 -> nothing to push for user 1
  Heap empty, loop ends.
  
  Return [6, 5]  ✓ matches expected [6, 5]

unfollow(1, 2)
  user_following[1].discard(2) -> user_following[1] = {}

getNewsFeed(1)
  relevant_users = {} | {1} = {1}
  For user 1: push (-0, 5, 1, 0)
  Pop -> recent_tweet_ids = [5]
  Return [5]  ✓ matches expected [5]
```

Every step matches the expected output from the prompt. 

Let me also spot-check my "more than 10 tweets from one followee" edge case mentally: if user 2 posted tweets with timestamps 0 through 14 (15 tweets total) and user 1 follows only user 2, `getNewsFeed(1)` would push user 2's *last* tweet (timestamp 14) onto the heap initially, then the loop would pop-and-push-next exactly 10 times, walking backward through user 2's list from index 14 down to index 5, giving the 10 most recent — timestamps 14 down to 5 — correctly stopping at 10 without ever needing to look at timestamps 0–4. That confirms the bounded pop-and-replenish logic does the right thing even with a single prolific followee, not just with many followees.

No bugs surfaced — the negated-timestamp trick and the index-decrementing "replenish" step both held up under trace.

**Interviewer:** Nice, clean trace, and I like that you stress-tested the single-prolific-followee case in your head rather than just leaving it as an assumption. That's a wrap.

---

# FINAL ASSESSMENT (Interviewer)

**Clarity:** Strong. You correctly identified upfront that tweetId ordering can't be trusted and that you need your own logical clock — that's a detail a lot of candidates miss and it would've caused a subtle bug three steps later if you hadn't caught it in Step 1.

**Correctness:** Solution matches the worked example exactly, and you proactively reasoned through a tricky edge case (single followee with >10 tweets) that the given example doesn't actually exercise, without me having to prompt you for it.

**Complexity:** This is the strongest part of the round. You correctly diagnosed that brute-force `getNewsFeed` scales with *total system-wide tweet volume*, and that the fix isn't about avoiding a full sort in the abstract — it's specifically about recognizing this as a **bounded k-way merge**, where k is capped by follow-count (≤500) rather than tweet count (≤3×10⁴). That's a meaningfully different, better bound, and you named it precisely rather than just saying "use a heap."

**Communication:** You clearly narrated the heap mechanics — the negation trick for simulating a max-heap, and the "pop one, replenish with that same user's next" pattern — which is exactly the part of this problem most candidates fumble through silently.

**One thing to tighten up:** In a real onsite I'd probe your `defaultdict` usage a bit — using `defaultdict(list)` for `user_tweets` means calling `getNewsFeed` for a userId that's never posted silently creates an empty list entry for them in the dict. Functionally harmless here, but worth flagging out loud as a design choice ("this could leak memory over millions of distinct never-posting users queried" is the kind of thing I'd want to hear you preempt, even if you conclude it's an acceptable trade-off for this problem's scale).

**Amazon Leadership Principles tie-in:** This is a great vehicle for **Customer Obsession** — a news feed's entire value proposition is showing users the most *relevant*, most *recent* content fast, and your optimization directly served that (bounding work by "how many people do you care about" rather than "how much data exists globally" mirrors real feed-ranking systems). It also ties into **Dive Deep** — you didn't stop at "use a heap," you interrogated *why* a heap, what bound it actually gives you (k, not T), and stress-tested an edge case that wasn't handed to you. That's the kind of depth Amazon likes to hear paired with a system-design-adjacent problem like this one.
