import datetime
from api.models import Incident, AffectedStation, Notification


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
                                           incident=incident, date=datetime.now())
                        obj.save()
                        inc_updated.append(incident.id)
                    affected_stations.remove(station)
        # If there are stations not related to active incidents
        # Create new incident
        if len(affected_stations) > 0:
            incident = Incident(status=1)
            incident.save()
            for station in affected_stations:
                obj = AffectedStation(
                    incident=incidents[0], affected_station=station)
                obj.save()
    else:
        # If there is no active incidents
        # Create incident
        incident = Incident(status=1)
        incident.save()

        # Create notification
        noti = Notification(tweet_id=tweet_id,
                            incident=incident, date=datetime.now())
        noti.save()

        # Add affected stations to incident
        for station in affected_stations:
            af_st = AffectedStation(
                incident=incident, affected_station=station)
            af_st.save()
