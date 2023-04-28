from api.modules.scrapping import get_tweets
from datetime import timedelta
from api.models import Line
import os
from django.conf import settings
import datetime

def update_status():
    """
    Update status of all lines based on tweets from the last 3 minutes

    Parameters:
        None
    Returns:
        Returns True if the process was successful
    """

    # Get the current datetime
    now = datetime.datetime.now()

    # Format the datetime as a string
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Open a log file and write the datetime string to it
    file = open(os.path.join(settings.PROJECT_ROOT, "../api/controllers/log.txt"), 'a')
    file.write(date_string + '\n')
    file.close()

    # Get tweets that were posted within the last 3 minutes
    tweets = get_tweets(timedelta(minutes=3))

    # Loop through the tweets and update the status of the affected lines in the database
    for tweet in tweets:
        # Get the type of the tweet ("O" for outage, "M" for maintenance, or None for other types)
        type = tweet.get_type()

        # If the tweet type is outage or maintenance, update the status of the affected lines
        if type:
            # Get the IDs of the affected lines
            affected_lines = tweet.get_lines()

            # Loop through the affected lines and update their status in the database
            for affected_line in affected_lines:
                try:
                    Line.objects.filter(pk=affected_line).update(status=type)
                except Line.DoesNotExist:
                    pass

                # TODO: Affected stations
                # TODO: Create incidents, update date of incidents
    return True


def renew_status():
    """
    Renew status of all lines to "O" (Operational)
    if the status is "U" (Under maintenance) do not change it

    Parameters:
        None
    
    Returns:
        Returns True if the status of all lines has been updated
    """
    lines = Line.objects.filter(status__in=["P", "M"])
    for line in lines:
        line.status = "O"
        line.save()
    return True