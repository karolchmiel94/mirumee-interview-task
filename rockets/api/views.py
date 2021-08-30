import json
from django.http.response import HttpResponse

from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from spacex_api_service.service import get_cores_data


@api_view(['GET'])
def get_cores(request):
    """
    query parameters:
        - cores_number: integer
          description: Number of the most popularly used cores
          paramType: query
          default: 5
        - successful: boolean
          paramType: query
          default: false
        - planned: boolean
          paramType: query
          default: false
    """
    core_number = request.query_params.get('cores_number')
    if core_number:
        try:
            core_number = int(core_number)
        except ValueError as e:
            return Response(
                'Cores number has to be integer.', status=status.HTTP_400_BAD_REQUEST
            )
    successful_flights = request.query_params.get('successful') == 'true'
    planned = request.query_params.get('planned') == 'true'
    try:
        cores_data = get_cores_data(core_number, successful_flights, planned)
        return Response(cores_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
