from datetime import datetime
import os
from dateutil.parser import isoparse
import uuid
import basistheory
import pytest
from pytest import approx
from basistheory import request_options
from basistheory.api import tokens_api, tokenize_api, applications_api
from basistheory.request_options import RequestOptions

tokens_to_delete = []
application = None
tokenize_client = None
tokens_client = None
request_options = None

@pytest.fixture(scope="module", autouse=True)
def setup():
    global application
    global tokenize_client
    global request_options

    configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api-dev.basistheory.com",
      api_key = os.environ.get('BT_API_KEY')
    ) 
    request_options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    application = applications_client.get_by_key(request_options=request_options)
    tokenize_client = tokenize_api.TokenizeApi(api_client)
    tokens_client = tokens_api.TokensApi(api_client)

    yield

    for token_id in tokens_to_delete:
        tokens_client.delete(token_id)


def test_tokenize(): 
    request = {
      "first_name": "Gonew",
      "last_name": "Webuino",
      "card": {
        "type": "card",
        "data": {
          "number": "4242424242424242",
          "expiration_month": 12,
          "expiration_year": 2025,
          "cvc": "123"
        }
      }
    }
    created_tokens = tokenize_client.tokenize(body=request, request_options=request_options)

    tokens_to_delete.append(created_tokens['first_name'])
    tokens_to_delete.append(created_tokens['last_name'])
    tokens_to_delete.append(created_tokens['card']['id'])

    card_token = created_tokens['card']
    
    assert card_token['type'] == 'card'
    assert card_token['data'] is not None
    assert card_token['tenant_id'] == application.tenant_id
    assert card_token['created_by'] == application.id
    assert datetime.utcnow().timestamp() - datetime.utcfromtimestamp(isoparse(card_token['created_at']).timestamp()).timestamp() == approx(0, abs=3)
    assert card_token['privacy']['classification'] == 'pci'
    assert card_token['privacy']['impact_level'] == 'high'
    assert card_token['privacy']['restriction_policy'] == 'mask'





