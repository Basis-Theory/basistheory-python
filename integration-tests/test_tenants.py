from datetime import datetime
from http import HTTPStatus
import os
import uuid
import basistheory
import pytest
from pytest import approx
from basistheory.api import applications_api, tenants_api
from basistheory.exceptions import NotFoundException
from basistheory.model.create_application_request import CreateApplicationRequest
from basistheory.model.update_application_request import UpdateApplicationRequest
from basistheory.request_options import RequestOptions

applications_to_delete = []
tenant = None
applications_client = None
tenants_client = None
options = None

@pytest.fixture(scope="module", autouse=True)
def setup():
    global tenant
    global applications_client
    global options

    configuration = basistheory.Configuration(
      host = "https://api-dev.basistheory.com",
      api_key = os.environ.get('BT_MANAGEMENT_API_KEY')
    ) 
    options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    tenants_client = tenants_api.TenantsApi(api_client)
    tenant = tenants_client.get(request_options=options)

    yield

    for app_id in applications_to_delete:
        applications_client.delete(app_id)


# def test_create(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)

#     applications_to_delete.append(application.id)

#     assert_application(application, request)

# def test_get(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)
#     applications_to_delete.append(application.id)

#     retrieved_applications = applications_client.get(id=[application.id])

#     assert_application(retrieved_applications.data[0], request)    

# def test_get_by_id(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)
#     applications_to_delete.append(application.id)

#     retrieved_application = applications_client.get_by_id(id=application.id)

#     assert_application(retrieved_application, request)        

# def test_get_by_key(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)
#     applications_to_delete.append(application.id)

#     configuration2 = basistheory.Configuration(
#       host = "https://api-dev.basistheory.com",
#       api_key = application.key
#     ) 
#     api_client2 = basistheory.ApiClient(configuration2)
#     applications_client2 = applications_api.ApplicationsApi(api_client2)

#     updatedRequestOptions = RequestOptions(api_key=application.key, correlation_id=uuid.uuid4().__str__())

#     retrieved_application = applications_client2.get_by_key(request_options=updatedRequestOptions)

#     assert_application(retrieved_application, request) 

# def test_update(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)

#     applications_to_delete.append(application.id)

#     update_request = UpdateApplicationRequest(
#       name="New name"
#     )
#     updated_application = applications_client.update(id=application.id,update_application_request=update_request)

#     assert updated_application.name == update_request.name
#     assert updated_application.modified_by is not None
#     assert updated_application.modified_at is not None

# def test_regenerate_key(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)

#     applications_to_delete.append(application.id)

#     regenerated_application = applications_client.regenerate_key(id=application.id)

#     assert application.key != regenerated_application.key

# def test_delete(): 
#     request = CreateApplicationRequest(
#       name="Test App",
#       type="server_to_server", 
#       permissions=["token:general:create", "token:general:read:low"]
#     )
#     application = applications_client.create(create_application_request=request)
#     applications_client.delete(application.id)

#     try:
#         error = applications_client.get_by_id(application.id)
#     except NotFoundException as error:
#         assert error.status == HTTPStatus.NOT_FOUND

def assert_application(application, request):
    assert application.id is not None
    assert application.tenant_id == tenant.id
    assert application.name == request.name
    assert application.type == request.type 
    assert application.created_by is not None
    assert datetime.utcnow().timestamp() - datetime.utcfromtimestamp(application.created_at.timestamp()).timestamp() == approx(0, abs=3)
    assert sorted(application.permissions) == sorted(request.permissions)





