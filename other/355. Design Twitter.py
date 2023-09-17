"""
https://leetcode.com/problems/design-twitter/
"""


import unittest


class User:
    def __init__(self, id):
        self.followed = {id}


class Twitter:
    def __init__(self):
        self.users: dict[int, User] = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        arr = []
        for i in range(len(self.tweets)):
            (tweetUserId, tweetId) = self.tweets[-1 - i]
            if tweetUserId in self.users[userId].followed:
                arr.append(tweetId)
            if len(arr) == 10:
                break
        return arr

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].followed.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user_followers_set = self.users[followerId].followed
        if followeeId in user_followers_set:
            user_followers_set.remove(followeeId)


class Test(unittest.TestCase):
    def test(self):
        obj = Twitter()
        obj.postTweet(1, 20)
        obj.postTweet(2, 21)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [20])
        obj.follow(1, 2)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [21, 20])
        obj.unfollow(1, 2)
        param_2 = obj.getNewsFeed(1)
        self.assertEqual(param_2, [20])


if __name__ == "__main__":
    unittest.main()
