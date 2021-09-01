import json

from rest_framework import viewsets, mixins
from rest_framework import status, permissions
from rest_framework.response import Response

from spacex_api.service import get_cores_data
from utilities.query_parser import parse_param_to_bool, parse_param_to_int
from .serializers import CoreSerializer, FavouriteCoreSerializer
from ..models import Core, FavouriteCore
from ..service import fetch_cores_if_not_in_database


class FetchCoreViewSet(viewsets.ViewSet):
    """
    query parameters:
        - cores_number: integer
          description: Number of the most popularly used cores
          paramType: query
        - successful: boolean
          description: Include or exclude successful missions
          paramType: query
        - planned: boolean
          description: Include or exclude planned missions
          paramType: query
    """

    def list(self, request, format=None):
        try:
            cores_number = parse_param_to_int(
                request.query_params, 'cores_number')
            successful_flights = parse_param_to_bool(
                request.query_params, 'successful')
            planned = parse_param_to_bool(request.query_params, 'planned')
            cores_data = get_cores_data(
                cores_number, successful_flights, planned)
            return Response(cores_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class CoreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    model = Core
    queryset = Core.objects.all()
    serializer_class = CoreSerializer

    def list(self, request, *args, **kwargs):
        fetch_cores_if_not_in_database()
        return super().list(request, *args, **kwargs)


class FavouriteCoreViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    model = FavouriteCore
    serializer_class = FavouriteCoreSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return FavouriteCore.objects.filter(user=self.request.user)
