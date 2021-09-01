from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from ..models import Core, FavouriteCore


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = ('id', 'core_id', 'reuse_count', 'mass_delivered')


class FavouriteCoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FavouriteCore
        fields = ('id', 'core', 'user')
