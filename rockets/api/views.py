import json

from rest_framework import viewsets, mixins
from rest_framework import status, permissions
from rest_framework.response import Response

from spacex_api.service import get_cores_data
from utilities.parser import parse_string_to_bool
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
        core_number = request.query_params.get('cores_number')
        if core_number is not None:
            try:
                core_number = int(core_number)
            except ValueError as e:
                return Response(
                    'Cores number has to be integer.',
                    status=status.HTTP_400_BAD_REQUEST,
                )
        successful_flights = request.query_params.get('successful')
        if successful_flights is not None:
            try:
                successful_flights = parse_string_to_bool(successful_flights)
            except ValueError as e:
                return Response(
                    'Parameter successful has to have value of True or False.',
                    status=status.HTTP_400_BAD_REQUEST,
                )
        planned = request.query_params.get('planned')
        if planned is not None:
            try:
                planned = parse_string_to_bool(planned)
            except ValueError as e:
                return Response(
                    'Parameter planned has to have value of True or False.',
                    status=status.HTTP_400_BAD_REQUEST,
                )
        try:
            cores_data = get_cores_data(
                core_number, successful_flights, planned)
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
