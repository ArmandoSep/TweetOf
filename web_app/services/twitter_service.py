import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# We could use a function or a class

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
print("API CLIENT:", api)

if __name__ == "__main__":
    user = api.get_user('elonmusk')
    print("TWITTER USER:", type(user))
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)


    tweets = api.user_timeline('elonmusk', tweet_mode='extended')
    print("TWEETS",type(tweet)) #> <class 'tweepy.models.Status'>
    print(type(tweets[0]))

    tweet = tweets[0]
    print(tweet.id)
    print(tweet.full_text)



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)