from modules.scrapping import get_tweets
from datetime import timedelta
from modules.tweet import Tweet

def update_status():
    #tweets = get_tweets(timedelta(minutes=2.5))
    tweets = [Tweet("1649256031610982402", "🟡(22:37)📢  Por invasión de motociclistas en el corredor de la carrera 45, a partir de este momento las líneas 1🚌 y 2🚌 de buses operan únicamente entre Universidad de Medellín y Hospital. 🔁 Estaremos informando. 🗣️ https://t.co/YE1a3R6FgX", "https://video.twimg.com/tweet_video/FuNVmDzX0AA2eCJ.mp4")]
    for tweet in tweets:
        type = tweet.get_type()
        if type:
            if type == "green" or type == "red":
                affected_lines = tweet.get_lines()
            else:
                affected_lines = tweet.get_lines()
                

                # TODO: Affected stations