class Twitter:

    def __init__(self):
        self.time_counter = 0
        self.user_tweets = defaultdict(list) # userId -> list of [count, tweetIds]
        self.user_following = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append([self.time_counter, tweetId])
        self.time_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_list = self.user_following[userId] | {userId}
        max_heap = []

        for candidate_user_id in user_list:
            user_tweet_list = self.user_tweets[candidate_user_id]
            if user_tweet_list:
                last_index = len(user_tweet_list) - 1
                tweet_timestamp, tweet_id = user_tweet_list[last_index]
                heapq.heappush(max_heap, (-tweet_timestamp, tweet_id, candidate_user_id, last_index))
            
        recent_tweet_ids = []

        while max_heap and len(recent_tweet_ids) < 10:
            negated_timestamp, tweet_id, owner_user_id, tweet_index = heapq.heappop(max_heap)
            recent_tweet_ids.append(tweet_id)

            next_index = tweet_index - 1
            if next_index >= 0:
                next_timestamp, next_tweet_id = self.user_tweets[owner_user_id][next_index]
                heapq.heappush(max_heap, (-next_timestamp, next_tweet_id, owner_user_id, next_index))
        
        return recent_tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)