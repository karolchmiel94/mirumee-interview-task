from django.db import models
from django.conf import settings


class Core(models.Model):
    core_id = models.CharField(max_length=255, unique=True)
    reuse_count = models.PositiveSmallIntegerField(default=0, blank=True)
    mass_delivered = models.IntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.core_id


class FavouriteCore(models.Model):
    core = models.ForeignKey(Core, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
    )

    def __str__(self):
        return self.core

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['core', 'user'], name='unique core for user'
            )
        ]
