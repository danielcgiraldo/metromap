from api.modules.scrapping import get_tweets
from datetime import timedelta
from api.models import Line
import os
from django.conf import settings
import datetime

def update_status():
    # Log
    now = datetime.datetime.now()
    # format the date as a string
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    file = open(os.path.join(settings.PROJECT_ROOT, "../api/controllers/log.txt"), 'a')
    file.write(date_string + '\n')
    file.close()


    tweets = get_tweets(timedelta(minutes=3))
    for tweet in tweets:
        type = tweet.get_type()
        if type:
            if type == "O" or type == "M":
                affected_lines = tweet.get_lines()
            else:
                affected_lines = tweet.get_lines()
            for affected_line in affected_lines:
                try:
                    Line.objects.filter(pk=affected_line).update(status=type)
                except Line.DoesNotExist:
                    pass

                # TODO: Affected stations
                # TODO: Create incidents
    return True