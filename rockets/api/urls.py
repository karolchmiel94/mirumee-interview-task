from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register('cores', views.CoresViewSet, basename='cores')
# router.register('cores', views.CoresList, basename='cores')


app_name = 'rockets'
urlpatterns = [
    # path('', include(router.urls)),
    path('cores/', views.get_cores, name='cores-list'),
]
