from django.http.response import HttpResponse

from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from spacex_api_service.service import get_cores_data


@api_view(['GET', ])
def get_cores(request):
    # validate query
    # get cores
    cores_data = get_cores_data(request.query_params)
    return HttpResponse('Returned method', status=status.HTTP_200_OK)
