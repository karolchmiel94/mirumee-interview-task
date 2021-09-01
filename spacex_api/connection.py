import json
import requests

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


def fetch_data_with_query(query=QUERY):
    request = requests.post(API_URL, json={'query': query})
    response = json.loads(request.text)
    if response.get('errors'):
        try:
            message = None
            for message in response.get('errors'):
                message += message + '. '
            message = response.get('errors')[0].get('message')
        except:
            raise SpacexAPIServiceException()
        raise SpacexAPIServiceException(message=message)
    return response
