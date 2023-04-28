from api.models import Line, Station


class Data:
    def __init__(self, line, station):
        """
        Constructor method for the Data class

        Args:
            line (Line): A Line object
            station (Station): A Station object
        """
        self.line = line
        self.station = station

    def get_data(self):
        """
        Return data according to request
        """
        data = {}

        # If a line is specified
        if self.line:
            # If a station is also specified
            if self.station:
                # Get the properties of the station
                estacion = self.station
                color = self.line.color
                sites_of_interest = estacion.sites_of_interest
                services = estacion.services

                # Add the color of the line to the data dictionary
                if self.line.id not in data:
                    data[self.line.id] = {}
                    data[self.line.id] = {"color": color}

                # Add the properties of the station to the data dictionary
                data[self.line.id][estacion.station] = {"sites_of_interest": sites_of_interest, "services": services}
            else:
                # If no station is specified, get all stations for the line ordered for id
                estaciones = Station.objects.filter(line=self.line).order_by("id")
                for estacion in estaciones:
                    # Get the properties of the station
                    color = self.line.color
                    sites_of_interest = estacion.sites_of_interest
                    services = estacion.services

                    # Add the color of the line to the data dictionary
                    if self.line.id not in data:
                        data[self.line.id] = {}
                        data[self.line.id] = {"color": color}

                    # Add the properties of the station to the data dictionary
                    data[self.line.id][estacion.station] = {"sites_of_interest": sites_of_interest, "services": services}

        else:
            # If no line is specified, get all lines
            lineas = Line.objects.all()
            for linea in lineas:
                # Get all stations for the line ordered for id
                estaciones = Station.objects.filter(line=linea).order_by("id")
                for estacion in estaciones:
                    # Get the properties of the station
                    if linea.id not in data:
                        data[linea.id] = {"color": linea.color, "stations": {}}

                    # Add the properties of the station to the data dictionary
                    data[linea.id]["stations"][estacion.station] = {"sites_of_interest": estacion.sites_of_interest, "services": estacion.services}

        return data
