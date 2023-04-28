from api.models import Line, Station

class Status:
    def __init__(self, line, station):
        self.line = line
        self.station = station

    def get_data(self):
        """
        Get the status data for a given line and station (if provided),
        or for all lines and stations if none are specified.
        
        Parameters:
            line (Line): The line to get the status for
            station (Station): The station to get the status for

        Returns:
            Returns a dictionary with line and station statuses
        """

        # Create an empty dictionary to hold the data
        data = {}
        
        # If a specific line is requested...
        if self.line:
            # If a specific station on the line is requested...
            if self.station:
                # Get the status for the specified station on the line
                if self.line.id not in data:
                    # If the line isn't already in the dictionary, add it with its status
                    data[self.line.id] = {}
                    data[self.line.id] = {"status": self.line.status} 
                # Add the status for the specified station to the dictionary
                data[self.line.id][self.station.station] = {"status": self.station.status}
            else:
                # Get the status for all stations on the line
                estaciones = Station.objects.filter(line=self.line).order_by("id")
                for estacion in estaciones:
                    if self.line.id not in data:
                        # If the line isn't already in the dictionary, add it with its status
                        data[self.line.id] = {}
                        data[self.line.id] = {"status": self.line.status} 
                    # Add the status for the current station to the dictionary
                    data[self.line.id][estacion.station] = {"status": estacion.status}
        else:
            # Get the status for all lines and stations
            lineas = Line.objects.all()
            for linea in lineas:
                estaciones = Station.objects.filter(line=linea).order_by("id")
                for estacion in estaciones:
                    if linea.id not in data:
                        # If the line isn't already in the dictionary, add it with its status and an empty stations dictionary
                        data[linea.id] = {"status": linea.status, "stations": {}} 
                    # Add the status for the current station to the dictionary under the appropriate line and stations
                    data[linea.id]["stations"][estacion.station] = {"status": estacion.status}
        
        # Return the dictionary containing the status data
        return data
