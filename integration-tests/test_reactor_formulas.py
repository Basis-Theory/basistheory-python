from datetime import datetime
from http import HTTPStatus
import uuid
import basistheory
import pytest
from pytest import approx
from basistheory import request_options
from basistheory.api import reactor_formulas_api, applications_api
from basistheory.exceptions import NotFoundException
from basistheory.model.create_reactor_formula_request import CreateReactorFormulaRequest
from basistheory.model.update_reactor_formula_request import UpdateReactorFormulaRequest
from basistheory.request_options import RequestOptions
from basistheory.model.reactor_formula_configuration import ReactorFormulaConfiguration
from basistheory.model.reactor_formula_request_parameter import ReactorFormulaRequestParameter

reactor_formulas_to_delete = []
application = None
reactor_formulas_client = None
request_options = None

request = CreateReactorFormulaRequest(
        name="My Private Reactor",
        description="Securely exchange token for another token",
        type="private",
        icon="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
        code=" \
            module.exports = async function (req) { \
                // Do something with `req.configuration.SERVICE_API_KEY`" \

                "return { \
                    raw: { \
                        foo: 'bar' \
                    } \
                }; \
            };",
        configuration=[
            ReactorFormulaConfiguration(
                name="SERVICE_API_KEY",
                description="Configuration description",
                type="string"
            )
        ],
        request_parameters=[
            ReactorFormulaRequestParameter(
                name="request_parameter_1",
                description="Request parameter description",
                type="string"
            ),
            ReactorFormulaRequestParameter(
                name="request_parameter_2",
                description="Request parameter description",
                type="boolean",
                optional=True
            )
        ]
    )

@pytest.fixture(scope="module", autouse=True)
def setup():
    global application
    global reactor_formulas_client
    global request_options

    configuration = basistheory.Configuration(
      host = "https://api-dev.basistheory.com",
      api_key = "key_dev_SRrj1yD7hWeovAxowdGMKG"
    ) 
    request_options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    application = applications_client.get_by_key(request_options=request_options)
    reactor_formulas_client = reactor_formulas_api.ReactorFormulasApi(api_client)

    yield
    
    for reactor_formula_id in reactor_formulas_to_delete:
        reactor_formulas_client.delete(id=reactor_formula_id)


def test_create(): 
    created_reactor_formula = reactor_formulas_client.create(create_reactor_formula_request=request)

    reactor_formulas_to_delete.append(created_reactor_formula.id)

    assert_reactor_formula(created_reactor_formula, request)

def test_get(): 
    created_reactor_formula = reactor_formulas_client.create(create_reactor_formula_request=request)

    reactor_formulas_to_delete.append(created_reactor_formula.id)

    reactor_formulas = reactor_formulas_client.get(name="My Private Reactor")

    assert_reactor_formula(reactor_formulas.data[0], request)

def test_get_by_id(): 
    created_reactor_formula = reactor_formulas_client.create(create_reactor_formula_request=request)

    reactor_formulas_to_delete.append(created_reactor_formula.id)

    reactor_formula = reactor_formulas_client.get_by_id(id=created_reactor_formula.id)

    assert_reactor_formula(reactor_formula, request)

def test_update(): 
    created_reactor_formula = reactor_formulas_client.create(create_reactor_formula_request=request)

    reactor_formulas_to_delete.append(created_reactor_formula.id)

    update_request = UpdateReactorFormulaRequest(
        name="My Private Reactor",
        type="private",
        code=" \
            module.exports = async function (req) { \
                // Do something with `req.configuration.SERVICE_API_KEY`" \

                "return { \
                    raw: { \
                        foo: 'bar' \
                    } \
                }; \
            };",
        configuration=[
            ReactorFormulaConfiguration(
                name="SERVICE_API_KEY",
                description="Configuration description",
                type="string"
            )
        ],
        request_parameters=[
            ReactorFormulaRequestParameter(
                name="request_parameter_1",
                description="Request parameter description",
                type="boolean",
                optional=True
            )
        ]
    )

    updated_reactor_formula = reactor_formulas_client.update(id=created_reactor_formula.id,update_reactor_formula_request=update_request)

    assert updated_reactor_formula.name == update_request.name
    assert updated_reactor_formula.modified_by is not None
    assert updated_reactor_formula.modified_at is not None

def test_delete(): 
    created_reactor_formula = reactor_formulas_client.create(create_reactor_formula_request=request)

    reactor_formulas_client.delete(id=created_reactor_formula.id)

    try:
        error = reactor_formulas_client.get_by_id(created_reactor_formula.id)
    except NotFoundException as error:
        assert error.status == HTTPStatus.NOT_FOUND

def assert_reactor_formula(reactor_formula, request):
    assert reactor_formula.id is not None
    assert reactor_formula.type == request.type
    assert reactor_formula.name == request.name
    assert reactor_formula.status == "verified"
    assert reactor_formula.description == request.description
    assert reactor_formula.icon == request.icon
    assert reactor_formula.code == request.code
    assert reactor_formula.created_by == application.id
    assert datetime.utcnow().timestamp() - datetime.utcfromtimestamp(reactor_formula.created_at.timestamp()).timestamp() == approx(0, abs=3)
    assert reactor_formula.configuration == request.configuration
    assert len(reactor_formula.request_parameters) == 2

    





