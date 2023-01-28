import feedparser
import tweepy
import time
import os
import keys

def api(): 
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Authentication credentials
EPISODE_FILE = 'latest_episode.txt'

# Authenticate with Twitter using tweepy
api = tweepy.API(auth)

# The RSS feed for the podcast
rss_feed = "https://allinchamathjason.libsyn.com/rss"

# Parse the RSS feed
feed = feedparser.parse(rss_feed)

# Set the delay between requests (in seconds)
DELAY = 86400  # 1 hour

while True:
    # Read the most recent episode that has been tweeted from the file
    if os.path.exists(EPISODE_FILE):
        with open(EPISODE_FILE, 'r') as f:
            newest_episode_title, newest_episode_link = f.read().strip().split('\n')
    else:
        newest_episode_title, newest_episode_link = None, None

    # Get the most recent episode's title and link
    feed = feedparser.parse(rss_feed)
    newest_episode_title = feed.entries[0].title
    newest_episode_link = feed.entries[0].link

    # If the most recent episode is different from the one that has been tweeted, tweet it
    if (newest_episode_title != newest_episode_title) or (newest_episode_link != newest_episode_link):
        tweet_text = f"It's time to go All In for another episode: {newest_episode_title} {newest_episode_link}"
        api.update_status(tweet_text)
        with open(EPISODE_FILE, 'w') as f:
            f.write(f"{newest_episode_title}\n{newest_episode_link}")

    # Wait for the specified delay before checking for new episodes again
    time.sleep(DELAY)