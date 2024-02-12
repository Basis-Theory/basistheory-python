from datetime import datetime
from http import HTTPStatus
import os
import uuid
import basistheory
import pytest
from pytest import approx
from basistheory.api import applications_api, reactors_api, tokens_api
from basistheory.exceptions import NotFoundException
from basistheory.model.create_reactor_request import CreateReactorRequest
from basistheory.model.create_token_request import CreateTokenRequest
from basistheory.model.react_request import ReactRequest
from basistheory.model.update_reactor_request import UpdateReactorRequest
from basistheory.request_options import RequestOptions

reactors_to_delete = []
application = None
reactors_client = None
request_options = None

request = None


@pytest.fixture(scope="module", autouse=True)
def setup():
    global application
    global reactor_formulas_client
    global reactors_client
    global react_client
    global tokens_client
    global request_options
    global reactor_formula
    global request

    configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api.flock-dev.com",
      api_key = os.environ.get('BT_MANAGEMENT_API_KEY')
    )
    private_configuration = basistheory.Configuration(
      host = os.environ.get('BT_API_URL') or "https://api.flock-dev.com",
      api_key = os.environ.get('BT_API_KEY')
    )
    request_options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    private_api_client = basistheory.ApiClient(private_configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    application = applications_client.get_by_key(request_options=request_options)
    reactors_client = reactors_api.ReactorsApi(api_client)
    react_client = reactors_api.ReactorsApi(private_api_client)
    tokens_client = tokens_api.TokensApi(private_api_client)
    request = CreateReactorRequest(
        name="My Reactor",
        code=" \
             module.exports = async function (req) { \
                 // Do something with `req.configuration.SERVICE_API_KEY`" \

                 "return { \
                     raw: { \
                         foo: 'bar' \
                     } \
                 }; \
             };",
        configuration={
            "SERVICE_API_KEY": "test"
        }
    )

    yield

    for reactor_id in reactors_to_delete:
        reactors_client.delete(id=reactor_id)


def test_create():
    created_reactor = reactors_client.create(create_reactor_request=request)

    reactors_to_delete.append(created_reactor.id)

    assert_reactor(created_reactor, request)


def test_react():
    created_token = tokens_client.create(create_token_request=CreateTokenRequest(type="card", data={
        "number": "4242424242424242",
        "expiration_month": 12,
        "expiration_year": 2025,
        "cvc": "123"
    }))

    react_request = ReactRequest(args={
        "card": f"{{{{ {created_token.id }}}}}"
    })

    react_response = react_client.react(id=os.environ.get('BT_CARD_REACTOR_ID'), react_request=react_request)

    assert react_response.raw is not None


def test_get():
    created_reactor = reactors_client.create(create_reactor_request=request)

    reactors_to_delete.append(created_reactor.id)

    reactors = reactors_client.get(id=[created_reactor.id])

    assert_reactor(reactors.data[0], request)


def test_get_by_id():
    created_reactor = reactors_client.create(create_reactor_request=request)

    reactors_to_delete.append(created_reactor.id)

    reactor = reactors_client.get_by_id(id=created_reactor.id)

    assert_reactor(reactor, request)


def test_update():
    created_reactor = reactors_client.create(create_reactor_request=request)

    reactors_to_delete.append(created_reactor.id)

    update_request = UpdateReactorRequest(
        name="Updated name",
        code=" \
             module.exports = async function (req) { \
                 // Do something with `req.configuration.SERVICE_API_KEY`" \

                 "return { \
                     raw: { \
                         foo: 'bar' \
                     } \
                 }; \
             };",
        configuration={
            "SERVICE_API_KEY": "key_abcd245"
        }
    )

    updated_reactor = reactors_client.update(id=created_reactor.id,update_reactor_request=update_request)

    assert updated_reactor.name == update_request.name
    assert updated_reactor.code == update_request.code
    assert updated_reactor.modified_by is not None
    assert updated_reactor.modified_at is not None


def test_delete():
    created_reactor = reactors_client.create(create_reactor_request=request)

    reactors_client.delete(id=created_reactor.id)

    try:
        error = reactors_client.get_by_id(created_reactor.id)
    except NotFoundException as error:
        assert error.status == HTTPStatus.NOT_FOUND


def assert_reactor(reactor, request):
    assert reactor.id is not None
    assert reactor.tenant_id == application.tenant_id
    assert reactor.name == request.name
    assert reactor.created_by == application.id
    assert datetime.utcnow().timestamp() - datetime.utcfromtimestamp(reactor.created_at.timestamp()).timestamp() == approx(0, abs=3)
    assert reactor.configuration == request.configuration
    assert reactor.code == request.code
