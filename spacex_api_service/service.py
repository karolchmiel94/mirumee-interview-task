import json
from urllib import parse
import requests

from . import api_models
from .exceptions import SpacexAPIServiceException, DataParsingException

API_URL = 'https://api.spacex.land/graphql'

QUERY = """query {
  launches {
    id
    rocket {
      first_stage {
        cores {
          core {
            id
            reuse_count
            missions {
              flight
            }
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


def fetch_cores_data(data):
    req = requests.post(API_URL, json={'query': QUERY})
    response = json.loads(req.text)
    if response.get('errors'):
        try:
            raise SpacexAPIServiceException(
                response.get('errors')[0].get('message'))
        except:
            raise SpacexAPIServiceException()
    try:
        return api_models.ApiData.parse_obj(response.get('data'))
    except:
        raise DataParsingException()


def get_cores_data(data):
    cores = fetch_cores_data(data)  # fetch data from external api
    # calculate overall payload mass for each core
    # sort cores by reused times
    # return list
    return cores
