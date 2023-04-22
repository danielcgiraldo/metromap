from django.http import JsonResponse
from api.modules.scrapping import get_tweets
from datetime import timedelta
from api.models import Line


def update_status():
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