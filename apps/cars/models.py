from django.db import models

from apps.autoparks.models import Autopark
from core.models import BaseModel


class Car(BaseModel):
    class Meta:
        db_table = 'cars'

    id = models.IntegerField(primary_key=True, auto_created=True)
    model = models.CharField(max_length=25)
    price = models.IntegerField()
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine_volume = models.FloatField()
    autopark = models.ForeignKey(Autopark, on_delete=models.CASCADE, related_name='cars', null=True)
