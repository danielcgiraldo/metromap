import snscrape.modules.twitter as sntwitter
from datetime import timedelta, datetime
from api.modules.tweet import Tweet
import pytz

def get_tweets(min_ago):
    """
    Returns tweets from @metrodemedellin since `datetime.utcnow() - min_ago`.

    Parameters:
        min_ago (timedelta): The time interval in the past to search for tweets.

    Returns:
        list: A list of `Tweet` objects that contain a GIF and meet the search criteria.
    """
    # Set the UTC timezone.
    tz_utc = pytz.timezone('UTC')

    # Calculate the start time for the search interval.
    date = tz_utc.localize(datetime.utcnow() - min_ago)

    # Initialize a scraper to search the @metrodemedellin profile for tweets.
    scraper = sntwitter.TwitterProfileScraper("metrodemedellin")

    # Initialize an empty list to store the tweets that meet the search criteria.
    tweets = []

    # Iterate over all the tweets in the profile.
    for tweet in scraper.get_items():
        content = tweet.rawContent

        # If the tweet is older than the search interval, stop searching.
        if (tweet.date < date):
            break

        # If the tweet is not a reply.
        if(content[0] != "@" and ''.join(content[0:2]) != "RT"):
            # If the tweet has a GIF, add it to the list of tweets.
            if(tweet.media):
                for medium in tweet.media:
                    if type(medium) == sntwitter.Gif:
                        tweets.append(Tweet(tweet.id, content, medium))
    
    # Return the list of tweets that meet the search criteria.
    return tweets
