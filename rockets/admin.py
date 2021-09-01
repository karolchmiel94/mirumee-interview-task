from django.contrib import admin

from .models import Core, FavouriteCore


@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    model = Core
    list_display = ('id', 'core_id', 'reuse_count', 'mass_delivered',)


@admin.register(FavouriteCore)
class FavouriteCoreAdmin(admin.ModelAdmin):
    model = FavouriteCore
    list_display = ('id', 'core', 'user',)
