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
from basistheory.model.create_tenant_invitation_request import CreateTenantInvitationRequest
from basistheory.model.tenant_invitation_status import TenantInvitationStatus
from basistheory.model.update_application_request import UpdateApplicationRequest
from basistheory.request_options import RequestOptions

applications_to_delete = []
applications_client = None
tenants_client = None
options = None

@pytest.fixture(scope="module", autouse=True)
def setup():
    global applications_client
    global options
    global tenants_client

    configuration = basistheory.Configuration(
      host = "https://api-dev.basistheory.com",
      api_key = "key_dev_9KZXo1jaeKtK2Z9NejCS11" # TODO change to env var once we get a mgmt key working for all
    ) 
    options = RequestOptions(api_key=configuration.api_key["apiKey"], correlation_id=uuid.uuid4().__str__())
    api_client = basistheory.ApiClient(configuration)
    applications_client = applications_api.ApplicationsApi(api_client)
    tenants_client = tenants_api.TenantsApi(api_client)

    yield

    for app_id in applications_to_delete:
        applications_client.delete(app_id)

def test_get(): 
    tenant = tenants_client.get(request_options=options)

    assert tenant.id is not None
    assert tenant.name is not None
    assert tenant.owner_id is not None
    assert tenant.created_at is not None

def test_get_tenant_usage_report(): 
    tenant_report = tenants_client.get_tenant_usage_report(request_options=options)

    assert tenant_report.token_report is not None

def test_get_invitations(): 
    invitations = tenants_client.get_invitations(request_options=options)

    assert invitations.data is not None
    
def test_get_members(): 
    members = tenants_client.get_members(request_options=options)

    assert members.data is not None

# TODO this endpoint is not working, it returns a list instead of an object
# def test_get_tenant_operation_report(): 
#     tenant_report = tenants_client.get_tenant_operation_report(request_options=options)

#     assert tenant_report.token_report is not None

def test_create_invitation():
    request = CreateTenantInvitationRequest(email="test@basistheory.com")

    invitation = tenants_client.create_invitation(create_tenant_invitation_request=request)

    assert invitation.id is not None
    assert invitation.email == request.email
    assert invitation.tenant_id is not None
    assert invitation.status is not None
    assert invitation.created_by is not None
    assert invitation.created_at is not None
    assert invitation.expires_at is not None

def test_delete_invitation():
    request = CreateTenantInvitationRequest(email="test@basistheory.com")

    invitation = tenants_client.create_invitation(create_tenant_invitation_request=request)

    tenants_client.delete_invitation(invitation_id=invitation.id)

    invitations = tenants_client.get_invitations(request_options=options)

    assert invitation.id not in map(lambda inv: inv.id, invitations.data)