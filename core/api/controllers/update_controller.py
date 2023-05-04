from api.modules.scrapping import get_tweets
from datetime import timedelta
from api.models import Line, Station, Incident, AffectedStation, Notification
import os
from django.conf import settings
import datetime
from api.modules.incident import create_incident


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
    file = open(os.path.join(settings.PROJECT_ROOT,
                "../api/controllers/log.txt"), 'a')
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

            if type in ["M", "O"]:
                # Update all line station statuses to "O" (Operational) or "M" (Major outage)
                lines = tweet.get_lines()
                for line in lines:
                    try:
                        # Update the status of the line
                        Line.objects.filter(pk=line).update(status=type)

                        # Get all stations of the line
                        stations = Station.objects.filter(line=line)

                        for station in stations:
                            # Update the status of the station
                            Station.objects.filter(
                                pk=station.id).update(status=type)

                    except Line.DoesNotExist or Station.DoesNotExist:
                        pass
            else:
                # Get the dictionary of affected lines and stations
                affected = tweet.get_stations()

                # Loop through the affected lines and update their status in the database
                for line, stations in affected.items():
                    try:
                        # Update the status of the line
                        Line.objects.filter(pk=line).update(status=type)

                        stations_len = len(stations)
                        if stations_len == 1:
                            # Very unlikely case
                            # Suppose that the affected station is closed but trains are still passing by
                            Station.objects.filter(
                                pk=stations[0]).update(status=type)
                            # Check if there is an incident active related to the station, if so update it
                            create_incident(stations, tweet.id)
                        elif stations_len == 2:
                            # Suppose that the affected stations are the interval where trains are passing by

                            pass
                        elif stations_len == 3:
                            # Suppose the station in the middle is closed and trains are passing by
                            pass
                        elif stations_len == 4:
                            # Suppose that each pair of affected stations are the interval where trains are passing by
                            pass
                        else:
                            # Not very clear case
                            # Register an incident related to all stations, update date of incidents
                            pass
                    except Line.DoesNotExist or Station.DoesNotExist:
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
