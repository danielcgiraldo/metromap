from django.db.models.signals import post_migrate
from django.dispatch import receiver
from api.models import Line, Alias, Station
import csv

@receiver(post_migrate)
def load_csvs(sender, **kwargs):
    
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
                obj = Station(id=row[0], line=line, sites_of_interest=row[2], services=row[3], status=row[4])
                obj.save()

    if not Alias.objects.exists():
        with open("./api/data/alias.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row
            for row in reader:
                line = Line.objects.get(id=row[1])
                station = Station.objects.get(id=row[2])
                # Create an instance of the model and save it to the database
                obj = Alias(alternate=row[0], line=line, station=station)
                obj.save()
    


    
