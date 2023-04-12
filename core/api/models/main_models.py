from django.db import models

""""
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
    status = models.TextChoices('O', 'P', 'M', 'U')
    color = models.CharField(max_length=6)
    type = models.TextChoices('M', 'C', 'TB', 'B')