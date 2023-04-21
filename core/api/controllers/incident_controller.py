from api.models import Incident as Incidents, AffectedStation, Notification
class Incident:
    def __init__(self, line, station):
        self.line = line
        self.station = station

    def get_data(self):
        """
        Return data according to request
        """
        # TODO: dt GET.VALUE

        data = {}
        # FIXME: Current classname to Incidents 
        incidents = Incidents.objects.filter(status=1)
        for incident in incidents:
            tweet_id = (Notification.objects.filter(incident=incident).first()).tweet_id
            if self.station:
                affected_stations = AffectedStation.objects.filter(incident=incident, affected_station=self.station)
            else:
                affected_stations = AffectedStation.objects.filter(incident=incident)
            for affected_station in affected_stations:
                station = affected_station.affected_station
                if self.station:
                    if self.station == station.station:
                        data[station.line][station.station] = {"status": station.status, "tweet_id": tweet_id}
                elif self.line:
                    if self.line == station.line:
                        if station.line.id not in data:
                            data[station.line.id] = {}
                        data[station.line.id][station.station] = {"status": station.status, "tweet_id": tweet_id}
                else:
                    if station.line.id not in data:
                        data[station.line.id] = {}
                    data[station.line.id][station.station] = {"status": station.status, "tweet_id": tweet_id}
        return data