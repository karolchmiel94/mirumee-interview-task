from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cores', views.CoreViewSet, basename='cores')
router.register(
    'favourite-cores', views.FavouriteCoreViewSet, basename='favourite-cores'
)
router.register('get-cores', views.FetchCoreViewSet, basename='get-cores')


app_name = 'rockets'
urlpatterns = [
    path('', include(router.urls)),
]
