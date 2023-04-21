from api.models import Line, Station

class Status:
    def __init__(self, line, station):
        self.line = line
        self.station = station

    def get_data(self):
        """
        Get the status data for a given line and station (if provided),
        or for all lines and stations if none are specified.
        Returns a dictionary with line and station statuses.
        """
        data = {}
        if self.line:
            if self.station:
                # Get status for specific station on a line
                if self.line.id not in data:
                    data[self.line.id] = {}
                    data[self.line.id] = {"status": self.line.status} 
                data[self.line.id][self.station.station] = {"status": self.station.status}
            else:
                # Get status for all stations on a line
                estaciones = Station.objects.filter(line=self.line).order_by("id")
                for estacion in estaciones:
                    if self.line.id not in data:
                        data[self.line.id] = {}
                        data[self.line.id] = {"status": self.line.status} 
                    data[self.line.id][estacion.station] = {"status": estacion.status}
        else:
            # Get status for all lines and stations
            lineas = Line.objects.all()
            for linea in lineas:
                estaciones = Station.objects.filter(line=linea).order_by("id")
                for estacion in estaciones:
                    if linea.id not in data:
                        data[linea.id] = {"status": linea.status, "stations": {}} 
                        print(linea.id, estacion.station)
                    data[linea.id]["stations"][estacion.station] = {"status": estacion.status}
        return data