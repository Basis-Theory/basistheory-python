# Basis Theory Python SDK

[![Release](https://github.com/Basis-Theory/basistheory-python/actions/workflows/release.yml/badge.svg)](https://github.com/Basis-Theory/basistheory-python/actions/workflows/release.yml)

The [Basis Theory](https://basistheory.com/) Python SDK for Python >=3.7

## Installation
### pip install

From the git repository

```sh
pip install git+https://github.com/Basis-Theory/basistheory-python.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Basis-Theory/basistheory-python.git`)

Then import the package:

```python
import basistheory
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import basistheory
```

### Locally
To install your latest changes locally run:

`python3 -m pip install .`

## Documentation

If you need any assistance, please contact support@basistheory.com at this time.

### Client Methods

All URIs are relative to *https://api.basistheory.com*

Class | Method | HTTP request
------------ | ------------- | -------------
*TokensApi* | [**create**](docs/TokensApi.md#create) | **POST** /tokens
*TokensApi* | [**delete**](docs/TokensApi.md#delete) | **DELETE** /tokens/{id}
*TokensApi* | [**get_by_id**](docs/TokensApi.md#get_by_id) | **GET** /tokens/{id}
*TokensApi* | [**list**](docs/TokensApi.md#list) | **GET** /tokens

### Models

- [EncryptionKey](docs/EncryptionKey.md)
- [EncryptionMetadata](docs/EncryptionMetadata.md)
- [PaginatedTokenList](docs/PaginatedTokenList.md)
- [Pagination](docs/Pagination.md)
- [Token](docs/Token.md)

## Usage

### Per-request configuration

All of the client methods accept an optional `RequestOptions` object.<br>This is
used if you want to set a [correlation ID](https://docs.basistheory.com/api-reference/?shell#request-correlation) or if you want to set a per-request [`BT-API-KEY`](https://docs.basistheory.com/api-reference/?shell#authentication)

```python
import uuid
import basistheory
from basistheory.request_options import RequestOptions

request_options = RequestOptions(api_key="API KEY", correlation_id=uuid.uuid4())
```

### Client Configuration

Each Api client can be configured to use a custom API url and client-wide [`BT-API-KEY`](https://docs.basistheory.com/api-reference/?shell#authentication).

```python
import basistheory
from basistheory.api import tokens_api

configuration = basistheory.Configuration(
    host = "https://token-proxy.somedomain.com",
    api_key = "API KEY"
)

with basistheory.ApiClient(configuration) as api_client:
    # Create a token client w/ global configuration for all requests
    token_client = tokens_api.TokensApi(api_client)
```

### Getting Started

Quick example creating a token and then retrieving it.

```python
import uuid
import basistheory
from pprint import pprint
from basistheory.api import tokens_api
from basistheory.model.create_token_request import CreateTokenRequest
from basistheory.request_options import RequestOptions

# Defining client wide api_key
configuration = basistheory.Configuration(
    api_key = "API KEY"
)

with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the tokens API client
    token_client = tokens_api.TokensApi(api_client)

    # Setting a correlation Id
    request_options = RequestOptions(correlation_id=uuid.uuid4().__str__())

    # Token request object
    request = CreateTokenRequest(type="token", data="My Secret Data")

    try:
        # Creating the token
        created_token = token_client.create(create_token_request=request, request_options=request_options)
        pprint(created_token)

        # Retrieving it (requires read permission on the token type classification and impact level)
        retrieved_token = token_client.get_by_id(id=created_token.id)
        pprint(retrieved_token)
    except basistheory.ApiException as e:
        print("Exception when calling TokensApi: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.basistheory.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationKeysApi* | [**create**](docs/ApplicationKeysApi.md#create) | **POST** /applications/{id}/keys |
*ApplicationKeysApi* | [**delete**](docs/ApplicationKeysApi.md#delete) | **DELETE** /applications/{id}/keys/{keyId} |
*ApplicationKeysApi* | [**get**](docs/ApplicationKeysApi.md#get) | **GET** /applications/{id}/keys |
*ApplicationKeysApi* | [**get_by_id**](docs/ApplicationKeysApi.md#get_by_id) | **GET** /applications/{id}/keys/{keyId} |
*ApplicationTemplatesApi* | [**get**](docs/ApplicationTemplatesApi.md#get) | **GET** /application-templates |
*ApplicationTemplatesApi* | [**get_by_id**](docs/ApplicationTemplatesApi.md#get_by_id) | **GET** /application-templates/{id} |
*ApplicationsApi* | [**create**](docs/ApplicationsApi.md#create) | **POST** /applications |
*ApplicationsApi* | [**delete**](docs/ApplicationsApi.md#delete) | **DELETE** /applications/{id} |
*ApplicationsApi* | [**get**](docs/ApplicationsApi.md#get) | **GET** /applications |
*ApplicationsApi* | [**get_by_id**](docs/ApplicationsApi.md#get_by_id) | **GET** /applications/{id} |
*ApplicationsApi* | [**get_by_key**](docs/ApplicationsApi.md#get_by_key) | **GET** /applications/key |
*ApplicationsApi* | [**regenerate_key**](docs/ApplicationsApi.md#regenerate_key) | **POST** /applications/{id}/regenerate |
*ApplicationsApi* | [**update**](docs/ApplicationsApi.md#update) | **PUT** /applications/{id} |
*DetokenizeApi* | [**detokenize**](docs/DetokenizeApi.md#detokenize) | **POST** /detokenize |
*EnrichmentsApi* | [**bank_account_verify**](docs/EnrichmentsApi.md#bank_account_verify) | **POST** /enrichments/bank-account-verify |
*LogsApi* | [**get**](docs/LogsApi.md#get) | **GET** /logs |
*LogsApi* | [**get_entity_types**](docs/LogsApi.md#get_entity_types) | **GET** /logs/entity-types |
*PermissionsApi* | [**get**](docs/PermissionsApi.md#get) | **GET** /permissions |
*ProxiesApi* | [**create**](docs/ProxiesApi.md#create) | **POST** /proxies |
*ProxiesApi* | [**delete**](docs/ProxiesApi.md#delete) | **DELETE** /proxies/{id} |
*ProxiesApi* | [**get**](docs/ProxiesApi.md#get) | **GET** /proxies |
*ProxiesApi* | [**get_by_id**](docs/ProxiesApi.md#get_by_id) | **GET** /proxies/{id} |
*ProxiesApi* | [**patch**](docs/ProxiesApi.md#patch) | **PATCH** /proxies/{id} |
*ProxiesApi* | [**update**](docs/ProxiesApi.md#update) | **PUT** /proxies/{id} |
*ReactorFormulasApi* | [**create**](docs/ReactorFormulasApi.md#create) | **POST** /reactor-formulas |
*ReactorFormulasApi* | [**delete**](docs/ReactorFormulasApi.md#delete) | **DELETE** /reactor-formulas/{id} |
*ReactorFormulasApi* | [**get**](docs/ReactorFormulasApi.md#get) | **GET** /reactor-formulas |
*ReactorFormulasApi* | [**get_by_id**](docs/ReactorFormulasApi.md#get_by_id) | **GET** /reactor-formulas/{id} |
*ReactorFormulasApi* | [**update**](docs/ReactorFormulasApi.md#update) | **PUT** /reactor-formulas/{id} |
*ReactorsApi* | [**create**](docs/ReactorsApi.md#create) | **POST** /reactors |
*ReactorsApi* | [**delete**](docs/ReactorsApi.md#delete) | **DELETE** /reactors/{id} |
*ReactorsApi* | [**get**](docs/ReactorsApi.md#get) | **GET** /reactors |
*ReactorsApi* | [**get_by_id**](docs/ReactorsApi.md#get_by_id) | **GET** /reactors/{id} |
*ReactorsApi* | [**patch**](docs/ReactorsApi.md#patch) | **PATCH** /reactors/{id} |
*ReactorsApi* | [**react**](docs/ReactorsApi.md#react) | **POST** /reactors/{id}/react |
*ReactorsApi* | [**react_async**](docs/ReactorsApi.md#react_async) | **POST** /reactors/{id}/react-async |
*ReactorsApi* | [**result_get_by_id**](docs/ReactorsApi.md#result_get_by_id) | **GET** /reactors/{id}/results/{requestId} |
*ReactorsApi* | [**update**](docs/ReactorsApi.md#update) | **PUT** /reactors/{id} |
*RolesApi* | [**get**](docs/RolesApi.md#get) | **GET** /roles |
*SessionsApi* | [**authorize**](docs/SessionsApi.md#authorize) | **POST** /sessions/authorize |
*SessionsApi* | [**create**](docs/SessionsApi.md#create) | **POST** /sessions |
*TenantsApi* | [**create_connection**](docs/TenantsApi.md#create_connection) | **POST** /tenants/self/connections |
*TenantsApi* | [**create_invitation**](docs/TenantsApi.md#create_invitation) | **POST** /tenants/self/invitations |
*TenantsApi* | [**delete**](docs/TenantsApi.md#delete) | **DELETE** /tenants/self |
*TenantsApi* | [**delete_connection**](docs/TenantsApi.md#delete_connection) | **DELETE** /tenants/self/connections |
*TenantsApi* | [**delete_invitation**](docs/TenantsApi.md#delete_invitation) | **DELETE** /tenants/self/invitations/{invitationId} |
*TenantsApi* | [**delete_member**](docs/TenantsApi.md#delete_member) | **DELETE** /tenants/self/members/{memberId} |
*TenantsApi* | [**get**](docs/TenantsApi.md#get) | **GET** /tenants/self |
*TenantsApi* | [**get_invitations**](docs/TenantsApi.md#get_invitations) | **GET** /tenants/self/invitations |
*TenantsApi* | [**get_members**](docs/TenantsApi.md#get_members) | **GET** /tenants/self/members |
*TenantsApi* | [**get_tenant_usage_report**](docs/TenantsApi.md#get_tenant_usage_report) | **GET** /tenants/self/reports/usage |
*TenantsApi* | [**owner_get**](docs/TenantsApi.md#owner_get) | **GET** /tenants/self/owner |
*TenantsApi* | [**resend_invitation**](docs/TenantsApi.md#resend_invitation) | **POST** /tenants/self/invitations/{invitationId}/resend |
*TenantsApi* | [**update**](docs/TenantsApi.md#update) | **PUT** /tenants/self |
*TenantsApi* | [**update_member**](docs/TenantsApi.md#update_member) | **PUT** /tenants/self/members/{memberId} |
*ThreeDSApi* | [**three_ds_authenticate_session**](docs/ThreeDSApi.md#three_ds_authenticate_session) | **POST** /3ds/sessions/{sessionId}/authenticate |
*ThreeDSApi* | [**three_ds_create_session**](docs/ThreeDSApi.md#three_ds_create_session) | **POST** /3ds/sessions |
*ThreeDSApi* | [**three_ds_get_challenge_result**](docs/ThreeDSApi.md#three_ds_get_challenge_result) | **GET** /3ds/sessions/{sessionId}/challenge-result |
*ThreeDSApi* | [**three_ds_get_session_by_id**](docs/ThreeDSApi.md#three_ds_get_session_by_id) | **GET** /3ds/sessions/{id} |
*TokenizeApi* | [**tokenize**](docs/TokenizeApi.md#tokenize) | **POST** /tokenize |
*TokensApi* | [**create**](docs/TokensApi.md#create) | **POST** /tokens |
*TokensApi* | [**delete**](docs/TokensApi.md#delete) | **DELETE** /tokens/{id} |
*TokensApi* | [**get**](docs/TokensApi.md#get) | **GET** /tokens |
*TokensApi* | [**get_by_id**](docs/TokensApi.md#get_by_id) | **GET** /tokens/{id} |
*TokensApi* | [**get_v2**](docs/TokensApi.md#get_v2) | **GET** /v2/tokens |
*TokensApi* | [**search**](docs/TokensApi.md#search) | **POST** /tokens/search |
*TokensApi* | [**search_v2**](docs/TokensApi.md#search_v2) | **POST** /v2/tokens/search |
*TokensApi* | [**update**](docs/TokensApi.md#update) | **PATCH** /tokens/{id} |


## Documentation For Models

- [AccessRule](docs/AccessRule.md)
- [Application](docs/Application.md)
- [ApplicationKey](docs/ApplicationKey.md)
- [ApplicationPaginatedList](docs/ApplicationPaginatedList.md)
- [ApplicationTemplate](docs/ApplicationTemplate.md)
- [AuthenticateThreeDSSessionRequest](docs/AuthenticateThreeDSSessionRequest.md)
- [AuthorizeSessionRequest](docs/AuthorizeSessionRequest.md)
- [BankVerificationRequest](docs/BankVerificationRequest.md)
- [BinDetails](docs/BinDetails.md)
- [BinDetailsBank](docs/BinDetailsBank.md)
- [BinDetailsCountry](docs/BinDetailsCountry.md)
- [BinDetailsProduct](docs/BinDetailsProduct.md)
- [CardDetails](docs/CardDetails.md)
- [Condition](docs/Condition.md)
- [CreateApplicationRequest](docs/CreateApplicationRequest.md)
- [CreateProxyRequest](docs/CreateProxyRequest.md)
- [CreateReactorFormulaRequest](docs/CreateReactorFormulaRequest.md)
- [CreateReactorRequest](docs/CreateReactorRequest.md)
- [CreateSessionResponse](docs/CreateSessionResponse.md)
- [CreateTenantConnectionRequest](docs/CreateTenantConnectionRequest.md)
- [CreateTenantConnectionResponse](docs/CreateTenantConnectionResponse.md)
- [CreateTenantInvitationRequest](docs/CreateTenantInvitationRequest.md)
- [CreateThreeDSSessionRequest](docs/CreateThreeDSSessionRequest.md)
- [CreateThreeDSSessionResponse](docs/CreateThreeDSSessionResponse.md)
- [CreateTokenRequest](docs/CreateTokenRequest.md)
- [CursorPagination](docs/CursorPagination.md)
- [GetApplications](docs/GetApplications.md)
- [GetLogs](docs/GetLogs.md)
- [GetPermissions](docs/GetPermissions.md)
- [GetProxies](docs/GetProxies.md)
- [GetReactorFormulas](docs/GetReactorFormulas.md)
- [GetReactors](docs/GetReactors.md)
- [GetTenantInvitations](docs/GetTenantInvitations.md)
- [GetTenantMembers](docs/GetTenantMembers.md)
- [GetTokens](docs/GetTokens.md)
- [GetTokensV2](docs/GetTokensV2.md)
- [Log](docs/Log.md)
- [LogEntityType](docs/LogEntityType.md)
- [LogPaginatedList](docs/LogPaginatedList.md)
- [Pagination](docs/Pagination.md)
- [PatchProxyRequest](docs/PatchProxyRequest.md)
- [PatchReactorRequest](docs/PatchReactorRequest.md)
- [Permission](docs/Permission.md)
- [Privacy](docs/Privacy.md)
- [ProblemDetails](docs/ProblemDetails.md)
- [Proxy](docs/Proxy.md)
- [ProxyPaginatedList](docs/ProxyPaginatedList.md)
- [ProxyTransform](docs/ProxyTransform.md)
- [ReactRequest](docs/ReactRequest.md)
- [ReactRequestAsync](docs/ReactRequestAsync.md)
- [ReactResponse](docs/ReactResponse.md)
- [Reactor](docs/Reactor.md)
- [ReactorFormula](docs/ReactorFormula.md)
- [ReactorFormulaConfiguration](docs/ReactorFormulaConfiguration.md)
- [ReactorFormulaPaginatedList](docs/ReactorFormulaPaginatedList.md)
- [ReactorFormulaRequestParameter](docs/ReactorFormulaRequestParameter.md)
- [ReactorPaginatedList](docs/ReactorPaginatedList.md)
- [Role](docs/Role.md)
- [SearchTokensRequest](docs/SearchTokensRequest.md)
- [SearchTokensRequestV2](docs/SearchTokensRequestV2.md)
- [StringStringKeyValuePair](docs/StringStringKeyValuePair.md)
- [Tenant](docs/Tenant.md)
- [TenantConnectionOptions](docs/TenantConnectionOptions.md)
- [TenantInvitationResponse](docs/TenantInvitationResponse.md)
- [TenantInvitationResponsePaginatedList](docs/TenantInvitationResponsePaginatedList.md)
- [TenantInvitationStatus](docs/TenantInvitationStatus.md)
- [TenantMemberResponse](docs/TenantMemberResponse.md)
- [TenantMemberResponsePaginatedList](docs/TenantMemberResponsePaginatedList.md)
- [TenantUsageReport](docs/TenantUsageReport.md)
- [ThreeDSAcsRenderingType](docs/ThreeDSAcsRenderingType.md)
- [ThreeDSAddress](docs/ThreeDSAddress.md)
- [ThreeDSAuthentication](docs/ThreeDSAuthentication.md)
- [ThreeDSCardholderAccountInfo](docs/ThreeDSCardholderAccountInfo.md)
- [ThreeDSCardholderAuthenticationInfo](docs/ThreeDSCardholderAuthenticationInfo.md)
- [ThreeDSCardholderInfo](docs/ThreeDSCardholderInfo.md)
- [ThreeDSCardholderPhoneNumber](docs/ThreeDSCardholderPhoneNumber.md)
- [ThreeDSDeviceInfo](docs/ThreeDSDeviceInfo.md)
- [ThreeDSMerchantInfo](docs/ThreeDSMerchantInfo.md)
- [ThreeDSMerchantRiskInfo](docs/ThreeDSMerchantRiskInfo.md)
- [ThreeDSMessageExtension](docs/ThreeDSMessageExtension.md)
- [ThreeDSMethod](docs/ThreeDSMethod.md)
- [ThreeDSMobileSdkRenderOptions](docs/ThreeDSMobileSdkRenderOptions.md)
- [ThreeDSPriorAuthenticationInfo](docs/ThreeDSPriorAuthenticationInfo.md)
- [ThreeDSPurchaseInfo](docs/ThreeDSPurchaseInfo.md)
- [ThreeDSRequestorInfo](docs/ThreeDSRequestorInfo.md)
- [ThreeDSSession](docs/ThreeDSSession.md)
- [ThreeDSVersion](docs/ThreeDSVersion.md)
- [Token](docs/Token.md)
- [TokenCursorPaginatedList](docs/TokenCursorPaginatedList.md)
- [TokenEnrichments](docs/TokenEnrichments.md)
- [TokenExtras](docs/TokenExtras.md)
- [TokenMetrics](docs/TokenMetrics.md)
- [TokenPaginatedList](docs/TokenPaginatedList.md)
- [TokenReport](docs/TokenReport.md)
- [UpdateApplicationRequest](docs/UpdateApplicationRequest.md)
- [UpdatePrivacy](docs/UpdatePrivacy.md)
- [UpdateProxyRequest](docs/UpdateProxyRequest.md)
- [UpdateReactorFormulaRequest](docs/UpdateReactorFormulaRequest.md)
- [UpdateReactorRequest](docs/UpdateReactorRequest.md)
- [UpdateTenantMemberRequest](docs/UpdateTenantMemberRequest.md)
- [UpdateTenantRequest](docs/UpdateTenantRequest.md)
- [UpdateTokenRequest](docs/UpdateTokenRequest.md)
- [User](docs/User.md)
- [ValidationProblemDetails](docs/ValidationProblemDetails.md)