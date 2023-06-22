from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError

from .models import Car


def car_filtered_queryset(query: QueryDict) -> QuerySet:
    qs = Car.objects.all()

    for k, v in query.items():
        match k:
            # key
            case 'id_' as id:
                qs = qs.filter(id__exact=v)
            # price
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt' as price:
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            # year
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            # seats
            case 'seats_gt':
                qs = qs.filter(seats__gt=v)
            case 'seats_lt':
                qs = qs.filter(seats__lt=v)
            case 'seats_gte':
                qs = qs.filter(seats__gte=v)
            case 'seats_lte':
                qs = qs.filter(seats__lte=v)
            # engine
            case 'engine_volume_gt':
                qs = qs.filter(engine_volume__gt=v)
            case 'engine_volume_lt':
                qs = qs.filter(engine_volume__lt=v)
            case 'engine_volume_gte':
                qs = qs.filter(engine_volume__gte=v)
            case 'engine_volume_lte':
                qs = qs.filter(engine_volume__lte=v)
            # price
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            # body
            case 'body_start':
                qs = qs.filter(body_type__startswith=v)
            case 'body_end':
                qs = qs.filter(body_type__endswith=v)
            case 'body_contain':
                qs = qs.filter(body_type__contains=v)
            # model
            case 'model_start':
                qs = qs.filter(model__startswith=v)
            case 'model_end':
                qs = qs.filter(model__endswith=v)
            case 'model_contain':
                qs = qs.filter(model__contains=v)
            case _:
                raise ValidationError({'details': f'key {k} is not allowed'})
    return qs
