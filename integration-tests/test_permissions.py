import os
import uuid
import basistheory
import pytest
from basistheory.api import permissions_api
from basistheory.request_options import RequestOptions

permissions_client = None

@pytest.fixture(scope="module", autouse=True)
def setup():
    global permissions_client

    configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api-dev.basistheory.com",
      api_key = os.environ.get('BT_MANAGEMENT_API_KEY')
    ) 
    api_client = basistheory.ApiClient(configuration)
    permissions_client = permissions_api.PermissionsApi(api_client)

    yield


def test_get(): 
    permissions = permissions_client.get(application_type="management")

    assert len(permissions) == 20


