import tweepy
import time

consumer_key = 'INSERT YOUR CONSUMER KEY'
consumer_secret = 'INSERT YOUR CONSUMER SECRET KEY'
access_token = 'INSERT YOUR ACCESS TOKEN'
access_token_secret = 'INSERT YOUR SECRET TOKEN'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)


search = "Finance"
numberOfTweets = 5


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)
        except StopIteration:
            break


# Be nice to your followers. Follow everyone!
# for friend in limit_handle(tweepy.Cursor(api.friends).items()):
#     if follower.name == 'Usernamehere':
#         print(friend.name)
#         follower.follow()

# Search for tweets containing a keyword
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Favorited the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
