import os
import basistheory
import pytest
from basistheory.api import logs_api

logs_client = None


@pytest.fixture(scope="module", autouse=True)
def setup():
    global logs_client

    configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api.flock-dev.com",
      api_key = os.environ.get('BT_MANAGEMENT_API_KEY')
    )
    api_client = basistheory.ApiClient(configuration)
    logs_client = logs_api.LogsApi(api_client)

    yield


def test_get():
    logs = logs_client.get()

    assert len(logs.data) >= 0


def test_get_entity_types():
    logs = logs_client.get_entity_types()

    assert len(logs) >= 0
