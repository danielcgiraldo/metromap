from django.db.models.signals import post_migrate
from django.dispatch import receiver
from api.models import Line, Alias, Station
import csv

@receiver(post_migrate)
def load_csvs(sender, **kwargs):
    """
    Load into database default values of lines,
    stations and alias

    Required Files
    /data
        alias.csv
        line.csv
        station.csv
    """
    
    if not Line.objects.exists():
        with open("./api/data/line.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            for row in reader:
                # Create an instance of the model and save it to the database
                obj = Line(id=row[0], status=row[1], color=row[2], type=row[3])
                obj.save()

    if not Station.objects.exists():
        with open("./api/data/station.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            for row in reader:
                line = Line.objects.get(id=row[1])
                # Create an instance of the model and save it to the database
                obj = Station(station=row[0], line=line, sites_of_interest=row[2], services=row[3], status=row[4])
                obj.save()

    if not Alias.objects.exists():
        with open("./api/data/alias.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            for row in reader:
                stations = Station.objects.filter(station=row[2])
                for station in stations:
                    # Create an instance of the model and save it to the database
                    obj = Alias.objects.create(alternate=row[0], station=station)
                    obj.save()
    


    
