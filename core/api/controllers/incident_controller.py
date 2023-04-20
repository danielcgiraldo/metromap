from api.models import Line, Station, Incident, AffectedStation, Notification
class Incident:
    def __init__(self, line, station):
        self.line = line
        self.station = station

    def get_data(self):
        """
        Return data according to request
        """
        # TODO: dt GET.VALUE

        
        incidents = Incident.objects.filter(status=1)

            
        return {"A": {"san_antonio": {"status": "O", "tweet_id": 123}}}