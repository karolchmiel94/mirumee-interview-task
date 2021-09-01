from spacex_api.service import get_cores_data
from .models import Core


def fetch_cores_if_not_in_database():
    if Core.objects.count() == 0:
        cores = get_cores_data(None, None, None)
        for core in cores:
            Core.objects.get_or_create(
                core_id=core[0], reuse_count=core[1], mass_delivered=core[2]
            )
