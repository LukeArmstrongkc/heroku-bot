# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "HgLU3UNLCcIU6zUNXV49Vby6q"
consumer_secret = "00pJZq7wvRlLAYwmMffFDKVfjo9DEq0gWvQiI66w26Id9f0LGz"
access_token = "138647252-8MROpqJEKnyth19VqWNzggFYHDQDnLdPsL4Vdv8G"
access_token_secret = "r0FDPD01NAK6cJBvYJsWkRYtG2ELUUnYMxInvSiFqg6Ku"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE