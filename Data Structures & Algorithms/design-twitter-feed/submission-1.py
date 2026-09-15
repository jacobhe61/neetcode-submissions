import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        ptrs = {}
        users = self.followers[userId].copy()
        users.add(userId)
        for f in users:
            if self.tweets[f]:
                ptrs[f] = len(self.tweets[f]) - 1
                heapq.heappush_max(heap, [self.tweets[f][ptrs[f]], f])
                ptrs[f] -= 1
        
        while len(feed) < 10 and heap:
            curr = heapq.heappop_max(heap)
            feed.append(curr[0][1])

            if ptrs[curr[1]] >= 0:
                heapq.heappush_max(heap, [self.tweets[curr[1]][ptrs[curr[1]]], curr[1]])
                ptrs[curr[1]] -= 1
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
