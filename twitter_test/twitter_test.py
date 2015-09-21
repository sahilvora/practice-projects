# http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# http://tweepy.readthedocs.org/en/v3.4.0/streaming_how_to.html
# https://github.com/tweepy/tweepy/blob/2f3c61efbd1744db4db699f36c8db87cdcfc51c3/examples/streaming.py

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_test_config import twitConfig

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(twitConfig.api_key, twitConfig.api_secret)
    auth.set_access_token(twitConfig.access_token, twitConfig.access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])