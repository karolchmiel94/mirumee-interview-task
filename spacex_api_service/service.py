import json
from urllib import parse
import requests
from operator import attrgetter

from . import api_models
from .exceptions import SpacexAPIServiceException, DataParsingException

API_URL = 'https://api.spacex.land/graphql'

QUERY = """query {
  launchesPast {
    id
    rocket {
      first_stage {
        cores {
          core {
            id
            reuse_count
          }
          reused
        }
      }
      rocket {
        id
        payload_weights {
          kg
          id
        }
      }
    }
    launch_success
    upcoming
  }
}
"""


def fetch_cores_data():
    req = requests.post(API_URL, json={'query': QUERY})
    response = json.loads(req.text)
    if response.get('errors'):
        try:
            message = response.get('errors')[0].get('message')
        except:
            raise SpacexAPIServiceException()
        raise SpacexAPIServiceException(message=message)
    try:
        return api_models.ApiData.parse_obj(response.get('data'))
    except:
        raise DataParsingException()


def get_return_data_with_weights(cores, count):
    data = []
    cores_occurencies = set()
    for launch in cores.launchesPast:
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
        if count is not None and len(data) == count:
            break
    return data


def get_cores_data(
    core_number=10, successful_flights=None, planned=None, raw_data=True
):
    cores = fetch_cores_data()  # fetch data from external api
    if not raw_data:
        cores.filter_launches(
            successful_flights, planned
        )  # filter by successful and planned
        cores.return_most_used(
            core_number
        )  # sort by reused number and returned requested count
    response = get_return_data_with_weights(
        cores, core_number
    )  # calculate overall payload mass for each core
    return response
