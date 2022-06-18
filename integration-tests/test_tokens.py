from datetime import datetime
from http import HTTPStatus
import os
import uuid

from retrying import retry

import basistheory
import pytest
from pytest import approx
from basistheory.api import tokens_api, applications_api
from basistheory.exceptions import NotFoundException
from basistheory.model.create_token_request import CreateTokenRequest
from basistheory.model.update_token_request import UpdateTokenRequest
from basistheory.model.search_tokens_request import SearchTokensRequest
from basistheory.model.privacy import Privacy
from basistheory.model.update_privacy import UpdatePrivacy
from basistheory.request_options import RequestOptions

tokens_to_delete = []
application = None
tokens_client = None
request_options = None


@pytest.fixture(scope="module", autouse=True)
def setup():
    global application
    global tokens_client
    global request_options

    configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api-dev.basistheory.com",
      api_key = os.environ.get('BT_API_KEY')
    ) 
    request_options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    application = applications_client.get_by_key(request_options=request_options)
    tokens_client = tokens_api.TokensApi(api_client)

    yield
    
    for token_id in tokens_to_delete:
        tokens_client.delete(token_id)


def test_create_tokens(): 
    privacyRequest = Privacy(restriction_policy="mask")
    request = CreateTokenRequest(type="token", data="My Secret Data", mask="{{ data | reveal_last: 4 }}", privacy=privacyRequest)

    created_token = tokens_client.create(create_token_request=request, request_options=request_options)

    tokens_to_delete.append(created_token.id)

    assert_token(created_token, request, False, True)


def test_get_tokens(): 
    request = CreateTokenRequest(type="token", data="My Secret Data", metadata = { "fooooo": "barrrrr" })

    created_token1 = tokens_client.create(create_token_request=request, request_options=request_options)
    created_token2 = tokens_client.create(create_token_request=request, request_options=request_options)
    tokens = tokens_client.get(metadata = { "fooooo": "barrrrr" })

    tokens_to_delete.append(created_token1.id)
    tokens_to_delete.append(created_token2.id)

    assert tokens.pagination.total_items >= 2

def test_update_tokens():
    create_request = CreateTokenRequest(type="token", data={ "foo": "bar", "bar": "foo" }, metadata={ "fooooo": "barrrrr" })

    created_token = tokens_client.create(create_token_request=create_request, request_options=request_options)

    maskUpdate = {"foo": "{{ data.foo }}", "newfoo": "{{ data | reveal_last: 4, '#' }}"}
    privacyUpdateRequest = UpdatePrivacy(restriction_policy="mask")
    update_request = UpdateTokenRequest(
        data={"foo": "newbar", "bar": None, "newfoo": "barbar"},
        metadata={"fooooo": "bar"},
        privacy=privacyUpdateRequest,
        mask=maskUpdate
    )
    
    updated_token = tokens_client.update(created_token.id, update_token_request=update_request, request_options=request_options)

    tokens_to_delete.append(created_token.id)

    assert updated_token.id == created_token.id
    assert updated_token.data == {"foo": "newbar", "newfoo": "barbar"}
    assert updated_token.metadata == {"fooooo": "bar"}
    assert updated_token.privacy.restriction_policy == "mask"
    assert updated_token.mask == maskUpdate


def test_get_token_by_id(): 
    request = CreateTokenRequest(type="token", data="My Secret Data")

    created_token = tokens_client.create(create_token_request=request, request_options=request_options)
    unencrypted_token = tokens_client.get_by_id(created_token.id)

    tokens_to_delete.append(created_token.id)

    assert_token(unencrypted_token, request, True, False)


def test_delete_token(): 
    request = CreateTokenRequest(type="token", data="My Secret Data")

    created_token = tokens_client.create(create_token_request=request, request_options=request_options)
    tokens_client.delete(created_token.id)

    try:
        error = tokens_client.get_by_id(created_token.id)
    except NotFoundException as error:
        assert error.status == HTTPStatus.NOT_FOUND


def test_search_tokens(): 
    randomKey = str(uuid.uuid4())
    randomValue = str(uuid.uuid4())
    request1 = CreateTokenRequest(type="social_security_number", data="123-45-6789", privacy=Privacy(impact_level="low"))
    request2 = CreateTokenRequest(type="employer_id_number", data="12-3456789", metadata = { randomKey: randomValue}, privacy=Privacy(impact_level="low"))

    created_token1 = tokens_client.create(create_token_request=request1, request_options=request_options)
    created_token2 = tokens_client.create(create_token_request=request2, request_options=request_options)

    tokens_to_delete.append(created_token1.id)
    tokens_to_delete.append(created_token2.id)

    searchTokensRequest = SearchTokensRequest(query = f'data:6789 AND metadata.{randomKey}:{randomValue}')

    assert_search_tokens(searchTokensRequest, created_token2.id)


@retry(stop_max_attempt_number=10, wait_fixed=1000)
def assert_search_tokens(request, expectedTokenId):
    tokens = tokens_client.search(search_tokens_request = request)

    assert tokens.pagination.total_items == 1
    assert expectedTokenId in map(lambda token: token.id, tokens.data)


def assert_token(token, request, assertData, masked):
    assert token.id is not None 
    assert token.type == 'token'
    assert token.data == request.data if assertData else True
    assert token.tenant_id == application.tenant_id
    assert token.created_by == application.id
    assert datetime.utcnow().timestamp() - datetime.utcfromtimestamp(token.created_at.timestamp()).timestamp() == approx(0, abs=3)
    assert token.privacy.classification == 'general'
    assert token.privacy.impact_level == 'high'
    assert token.privacy.restriction_policy == 'mask' if masked else token.privacy.restriction_policy == 'redact'
    assert token.mask == request.mask if masked else True
