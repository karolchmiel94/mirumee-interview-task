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
    # validate query
    core_number = request.query_params.get('cores_number')
    if core_number:
        try:
            core_number = int(core_number)
        except Exception as e:
            print(e)
    successful_flights = request.query_params.get('successful')
    if successful_flights:
        successful_flights = successful_flights == 'true'
    planned = request.query_params.get('planned')
    if planned:
        planned = planned == 'true'
    # get cores
    try:
        cores_data = get_cores_data(core_number, successful_flights, planned)
        return Response(cores_data.dict(), status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
