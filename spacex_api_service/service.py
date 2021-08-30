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


def fetch_cores_data(core_number, successful_flights, planned):
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


def get_cores_data(core_number=10, successful_flights=None, planned=None):
    cores = fetch_cores_data(
        core_number, successful_flights, planned
    )  # fetch data from external api
    # cores.launches.sort(key=attrgetter(
    #     'rocket.first_stage.cores[0].core.reuse_count'), reverse=True)
    for rocket in cores.launches:
        print('rocket_id: {rocket_id}'.format(rocket_id=rocket.id))
        print('first core reuse count: {num}'.format(
            num=rocket.rocket.first_stage.cores[0].core.reuse_count))
    cores.launches.sort(
        key=api_models.Rocket.first_stage.cores[0].core.reuse_count, reverse=True)
    # filter cores by number given in query
    # sort cores by reused times
    # calculate overall payload mass for each core
    # return list
    return cores
