from api.models import Incident, AffectedStation, Notification, Station
from django.utils import timezone


def create_incident(affected_stations, tweet_id):
    incidents = Incident.objects.filter(status=1)
    if incidents:
        # If there is active incidents
        # Check which stations are related to active incidents
        # Update incidents
        inc_updated = []
        for station in affected_stations:
            for incident in incidents:
                if AffectedStation.objects.filter(incident=incident, affected_station=station):
                    if incident.id not in inc_updated:
                        
                        obj = Notification(tweet_id=tweet_id,
                                           incident=incident, date=timezone.now())
                        obj.save()
                        inc_updated.append(incident.id)
                    affected_stations = affected_stations.exclude(pk=station.pk)
        # If there are stations not related to active incidents
        # Create new incident
        if len(affected_stations) > 0:
            incident = Incident(status=1)
            incident.save()
            for station in affected_stations:
                obj = AffectedStation(
                    incident=incidents[0], affected_station=station)
                obj.save()
            
            noti = Notification(tweet_id=tweet_id,
                                incident=incident, date=timezone.now())
            noti.save()
    else:
        # If there is no active incidents
        # Create incident
        incident = Incident(status=1)
        incident.save()

        # Create notification
        
        noti = Notification(tweet_id=tweet_id,
                            incident=incident, date=timezone.now())
        noti.save()

        # Add affected stations to incident
        for station in affected_stations:
            af_st = AffectedStation(
                incident=incident, affected_station=station)
            af_st.save()


def full_incident(line, tweet, type="O"):
    """
    Change the status of all stations of a line to the given type.
    """
    stations_of_line = Station.objects.filter(line=line)
    if type == "O":
        incidents = Incident.objects.filter(status=1)
        if incidents:
            for incident in incidents:
                affected_stations = AffectedStation.objects.filter(
                    incident=incident)
                affected_stations_len = len(affected_stations)
                station_count = 0
                for station in affected_stations:
                    if station in stations_of_line:
                        station_count += 1
                        station.status = "O"
                        station.save()
                if station_count == affected_stations_len:
                    # If the incident stations are all related to the line
                    incident.status = 0
                if station_count > 0:
                    
                    notif = Notification(tweet_id=tweet,
                                         incident=incident, date=timezone.now())
                    notif.save()
                incident.updated_at = timezone.now()
                incident.save()
    else:
        for station in stations_of_line:
            station.status = "M"
            station.save()
        incident = Incident(status=1)
        incident.save()
        for station in stations_of_line:
            affected_station = AffectedStation(
                incident=incident, affected_station=station)
            affected_station.save()
        
        notif = Notification(tweet_id=tweet,
                             incident=incident, date=timezone.now())
        notif.save()
