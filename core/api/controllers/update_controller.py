from modules.scrapping import get_tweets
from datetime import timedelta

def update_status():
    # datatime.now() - timedelta(minutes=2.5) = 5 minutes ago
    tweets = get_tweets(timedelta(minutes=2.5))
    for tweet in tweets:
        pass
