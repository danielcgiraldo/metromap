from api.models import Incidents, AffectedStation, Notification
class Incidents:
    def __init__(self, line, station, GET):
        self.line = line
        self.station = station
        self.dt = GET.get("dt", None)

    def get_data(self):
        """
        Get line and station statuses that have been 
        affected by an incident.

        Parameters:
            line (Line): The line to get the status for
            station (Station): The station to get the status for
            dt (datetime): The date to get the status for

        Returns:
            Returns a dictionary with line and station statuses
        """

        data = {}

        # Filter incidents based on date and status
        if self.dt:
            incidents = Incidents.objects.filter(date__gte=self.dt, status=1)
        else:
            incidents = Incidents.objects.filter(status=1)

        # Loop through incidents and retrieve tweet_id and affected stations
        for incident in incidents:
            tweet_id = (Notification.objects.filter(incident=incident).first()).tweet_id

            # Filter affected stations based on station or all affected stations
            if self.station:
                affected_stations = AffectedStation.objects.filter(incident=incident, affected_station=self.station)
            else:
                affected_stations = AffectedStation.objects.filter(incident=incident)

            # Loop through affected stations and store data in dictionary
            for affected_station in affected_stations:
                station = affected_station.affected_station

                if self.station:
                    # If station is specified in request, only include data for that station
                    if self.station == station.station:
                        data[station.line][station.station] = {"status": station.status, "tweet_id": tweet_id}
                elif self.line:
                    # If line is specified in request, only include data for that line
                    if self.line == station.line:
                        if station.line.id not in data:
                            data[station.line.id] = {}
                        data[station.line.id][station.station] = {"status": station.status, "tweet_id": tweet_id}
                else:
                    # If neither station nor line is specified in request, include all data
                    if station.line.id not in data:
                        data[station.line.id] = {}
                    data[station.line.id][station.station] = {"status": station.status, "tweet_id": tweet_id}

        return data