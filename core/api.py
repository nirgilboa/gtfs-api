import datetime

from django.contrib.gis.geos import Point
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet


class StationViewSet(GenericViewSet):

    @action(detail=False, url_path='search-by-route')
    def search_by_route(self, request):
        lat = request.GET.get('lat', None)
        long = request.GET.get('long', None)
        epoch_timestamp = request.GET.get('epoch_timestamp', None)
        route = request.GET.get('route', None)
        if lat is None:
            raise ValidationError(detail="lat is required")
        if long is None:
            raise ValidationError(detail='long is required')
        if timestamp is None:
            raise ValidationError(detail='timestamp is required')
        if route is None:
            raise ValidationError(detail='route is required')

        try:
            point = Point(x=float(long), y=float(lat))
        except (TypeError, ValueError):
            raise ValidationError(detail='Invalid lat/long coordinates')

        datetime.datetime.fromtimestamp(epoch_timestamp)





