from django.db import models

"""
    Entities that are directly related to the map operation

    Classes:
        Line
        Station
        Alias
        Incident
        Affected_Station
        Notification
"""

class Line(models.Model):
    """
    Module for Line table.

    Attributes:
        id (str)
        status ('O', 'P', 'M', 'U')
            status must be: O, P, M, U: operational, partial outage, major outage, under maintenance.
        color (str)
        type ('M', 'C', 'TB', 'B')
            type must be: M, C, TB, B: metro, cable, trolley and electric bus, bus.
    """
    id = models.CharField(max_length=1, primary_key=True)
    STATUS_CHOICES = [
        ('O', 'Operational'),
        ('P', 'Partial outage'),
        ('M', 'Major outage'),
        ('U', 'Under maintenance'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    color = models.CharField(max_length=6)
    TYPE_CHOICES = [
        ('M', 'Metro'),
        ('C', 'Cable'),
        ('TB', 'Trolley and electric bus'),
        ('B', 'Bus'),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

class Station(models.Model):
    id = models.AutoField(primary_key=True)
    line = models.ForeignKey(Line, on_delete=models.RESTRICT)
    station = models.CharField(max_length=100, default="unknown")
    sites_of_interest = models.JSONField(null=True)
    services = models.JSONField(null=True)
    STATUS_CHOICES = [
        ('O', 'Operational'),
        ('P', 'Partial outage (closed station with transit)'),
        ('M', 'Major outage'),
        ('U', 'Under maintenance'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    class Meta:
        unique_together = (('line', 'station'),)


class Alias(models.Model):
    id = models.AutoField(primary_key=True)
    alternate = models.CharField(max_length=100)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    
class Incident(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    status = models.BooleanField()

class AffectedStation(models.Model):
    id = models.AutoField(primary_key=True)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    affected_station = models.ForeignKey(Station, on_delete=models.CASCADE)

class Notification(models.Model):
    tweet_id = models.CharField(max_length=40, primary_key=True)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    date = models.DateTimeField()
    


""""
    Entities that are related to map and user interaction

    Classes:
        Report
        User
        
"""

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('V', 'Vehicles'),
        ('S', 'Stations'),
        ('L', 'Lines'),
        ('C', 'Contact means'),
        ('W', 'Webpage'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    description = models.CharField(max_length=250, null=True)
    date = models.DateTimeField()

class User(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    status = models.BooleanField()
    credits = models.IntegerField()
    secret_key = models.CharField(max_length=20, unique=True)
    public_key = models.CharField(max_length=20, unique=True)
    allowed_domains = models.JSONField()