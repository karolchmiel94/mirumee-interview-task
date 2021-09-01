import json
from urllib import parse
import requests
from operator import attrgetter

from . import api_models
from .connection import fetch_data_with_query
from .exceptions import DataParsingException


def fetch_and_parse_data():
    data = fetch_data_with_query()
    try:
        return api_models.ApiData.parse_obj(data.get('data'))
    except:
        raise DataParsingException()


def get_return_data_with_calculated_weights(cores, count):
    data = []
    cores_occurencies = set()
    for launch in cores.launchesPast:
        if count is not None and len(data) == count:
            break
        core_id = launch.rocket.first_stage.cores[0].core.id
        if core_id in cores_occurencies:
            continue
        else:
            cores_occurencies.add(core_id)
        used_count = launch.rocket.first_stage.cores[0].core.reuse_count
        weight = 0
        for mass in launch.rocket.rocket.payload_weights:
            weight += mass.kg
        data.append((core_id, used_count, weight))
    return data


def get_cores_data(cores_number=None, successful_flights=None, planned=None):
    cores = fetch_and_parse_data()  # fetch data from external api
    cores.filter_launches(
        successful_flights, planned
    )  # filter by successful and planned
    cores.return_most_used(
        cores_number
    )  # sort by reused number and returned requested count
    response = get_return_data_with_calculated_weights(
        cores, cores_number
    )  # calculate overall payload mass for each core
    return response
