from django.db import models

from apps.autoparks.models import Autopark
from apps.cars.choices.body_type_choices import BodyTypeChoices
from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from django.core import validators as V


class Car(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=25,
                             validators=(
                                 V.RegexValidator(RegExEnum.CAR_MODEL.pattern, RegExEnum.CAR_MODEL.msg),
                             ))
    price = models.IntegerField(validators=(
        V.MinValueValidator(0, 'Min value = 0'),
    ))
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=25, choices=BodyTypeChoices.choices)
    engine_volume = models.FloatField()
    autopark = models.ForeignKey(Autopark, on_delete=models.CASCADE, related_name='cars', null=True)
