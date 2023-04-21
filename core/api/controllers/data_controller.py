from api.models import Line, Station

class Data:
    def __init__(self, line, station):
        self.line = line
        self.station = station

    def get_data(self):
        """
        Return data according to request
        """
        data = {}
        if self.line:
            if self.station:
                estacion = self.station
                color = self.line.color
                sites_of_interest = estacion.sites_of_interest
                services = estacion.services
                if self.line.id not in data:
                        data[self.line.id] = {}
                data[self.line.id] = {"color": color} 
                data[self.line.id][estacion.station] = {"sites_of_interest": sites_of_interest, "services": services}
            
            else:
                estaciones = Station.objects.filter(line = self.line)
                for estacion in estaciones:
                    color = self.line.color
                    sites_of_interest = estacion.sites_of_interest
                    services = estacion.services
                    if self.line.id not in data:
                        data[self.line.id] = {}
                    data[self.line.id] = {"color": color} 
                    data[self.line.id][estacion.station] = {"sites_of_interest": sites_of_interest, "services": services}
                    
        else:
            lineas = Line.objects.all()
            for linea in lineas:
                estaciones = Station.objects.filter(line = linea)
                for estacion in estaciones:
                    color = linea.color
                    sites_of_interest = estacion.sites_of_interest
                    services = estacion.services
                    if linea.id not in data:
                        data[linea.id] = {}
                    data[linea.id] = {"color": color} 
                    data[linea.id][estacion.station] = {"sites_of_interest": sites_of_interest, "services": services}
        
        return data




                




            
                