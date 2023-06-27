from django.db import models


class BodyTypeChoices(models.TextChoices):
    Sedan = 'Sedan',
    Hatchback = 'Hatchback',
    SUV = 'SUV',
    Coupe = 'Coupe'
