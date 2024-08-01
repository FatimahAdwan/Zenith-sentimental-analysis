import tweepy
import configparser
import pandas as pd 
# read configs
config = configparser.ConfigParser() #create an instance of the configparser to read the configuration file
config.read("config.ini")

api_key = config["twitter"]["api_key"]
api_key_secret = config["twitter"]["api_key_secret"] 

access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) # Creates an API object for interacting with twitter API

# keyword used is the hastag #ZenithBankbringbackmymoney# and spec
keywords = "@ZenithBank OR #ZenithBankreturnmymoney OR #ZenithBank"
limit = 10000
#tweets = tweepy.cursor(api.search_tweets, q = keywords, count = 100, tweet_mood = "extended").items(limit)
tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, lang = "en", tweet_mode='extended').items(limit)
#creat dataframe 
columns = ['id', 'Time', 'User', 'Tweet', 'No of retweet', 'likes', 'Country',
       'Tweet source', 'Verified']
data = []
for tweet in tweets:
    data.append([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.full_text, tweet.retweet_count, tweet.favorite_count, tweet.user.location, tweet.source, tweet.user.verified])
df = pd.DataFrame(data, columns = columns)

df.to_csv("tweets10.csv")

#print(df)