# basistheory.TenantsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](TenantsApi.md#create_connection) | **POST** /tenants/self/connections | 
[**create_invitation**](TenantsApi.md#create_invitation) | **POST** /tenants/self/invitations | 
[**delete**](TenantsApi.md#delete) | **DELETE** /tenants/self | 
[**delete_connection**](TenantsApi.md#delete_connection) | **DELETE** /tenants/self/connections | 
[**delete_invitation**](TenantsApi.md#delete_invitation) | **DELETE** /tenants/self/invitations/{invitationId} | 
[**delete_member**](TenantsApi.md#delete_member) | **DELETE** /tenants/self/members/{memberId} | 
[**get**](TenantsApi.md#get) | **GET** /tenants/self | 
[**get_invitations**](TenantsApi.md#get_invitations) | **GET** /tenants/self/invitations | 
[**get_members**](TenantsApi.md#get_members) | **GET** /tenants/self/members | 
[**get_tenant_usage_report**](TenantsApi.md#get_tenant_usage_report) | **GET** /tenants/self/reports/usage | 
[**owner_get**](TenantsApi.md#owner_get) | **GET** /tenants/self/owner | 
[**resend_invitation**](TenantsApi.md#resend_invitation) | **POST** /tenants/self/invitations/{invitationId}/resend | 
[**update**](TenantsApi.md#update) | **PUT** /tenants/self | 
[**update_member**](TenantsApi.md#update_member) | **PUT** /tenants/self/members/{memberId} | 


# **create_connection**
> CreateTenantConnectionResponse create_connection(create_tenant_connection_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.create_tenant_connection_response import CreateTenantConnectionResponse
from basistheory.model.create_tenant_connection_request import CreateTenantConnectionRequest
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    create_tenant_connection_request = CreateTenantConnectionRequest(
        strategy="strategy_example",
        options=TenantConnectionOptions(
            domain_aliases=[
                "domain_aliases_example",
            ],
        ),
    ) # CreateTenantConnectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_connection(create_tenant_connection_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->create_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_connection_request** | [**CreateTenantConnectionRequest**](CreateTenantConnectionRequest.md)|  |

### Return type

[**CreateTenantConnectionResponse**](CreateTenantConnectionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation**
> TenantInvitationResponse create_invitation(create_tenant_invitation_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.tenant_invitation_response import TenantInvitationResponse
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.create_tenant_invitation_request import CreateTenantInvitationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    create_tenant_invitation_request = CreateTenantInvitationRequest(
        email="email_example",
        role="role_example",
    ) # CreateTenantInvitationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_invitation(create_tenant_invitation_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->create_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_invitation_request** | [**CreateTenantInvitationRequest**](CreateTenantInvitationRequest.md)|  |

### Return type

[**TenantInvitationResponse**](TenantInvitationResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.delete()
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> CreateTenantConnectionResponse delete_connection()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.create_tenant_connection_response import CreateTenantConnectionResponse
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_connection()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->delete_connection: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateTenantConnectionResponse**](CreateTenantConnectionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation**
> delete_invitation(invitation_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    invitation_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_invitation(invitation_id)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->delete_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member**
> delete_member(member_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    member_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_member(member_id)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->delete_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Tenant get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.tenant import Tenant
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitations**
> TenantInvitationResponsePaginatedList get_invitations()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.tenant_invitation_response_paginated_list import TenantInvitationResponsePaginatedList
from basistheory.model.tenant_invitation_status import TenantInvitationStatus
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    status = TenantInvitationStatus("PENDING") # TenantInvitationStatus |  (optional)
    page = 0 # int, none_type |  (optional)
    start = "start_example" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_invitations(status=status, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->get_invitations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **TenantInvitationStatus**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**TenantInvitationResponsePaginatedList**](TenantInvitationResponsePaginatedList.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members**
> TenantMemberResponsePaginatedList get_members()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.tenant_member_response_paginated_list import TenantMemberResponsePaginatedList
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    user_id = [
        "62ECB020-8429-30cc-01FF-CCfeEe150AC3",
    ] # [str], none_type |  (optional)
    page = 0 # int, none_type |  (optional)
    start = "start_example" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_members(user_id=user_id, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->get_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **[str], none_type**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**TenantMemberResponsePaginatedList**](TenantMemberResponsePaginatedList.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_usage_report**
> TenantUsageReport get_tenant_usage_report()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.tenant_usage_report import TenantUsageReport
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenant_usage_report()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->get_tenant_usage_report: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantUsageReport**](TenantUsageReport.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **owner_get**
> TenantMemberResponse owner_get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.tenant_member_response import TenantMemberResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.owner_get()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->owner_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantMemberResponse**](TenantMemberResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_invitation**
> TenantInvitationResponse resend_invitation(invitation_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.tenant_invitation_response import TenantInvitationResponse
from basistheory.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    invitation_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resend_invitation(invitation_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->resend_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  |

### Return type

[**TenantInvitationResponse**](TenantInvitationResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Tenant update(update_tenant_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.tenant import Tenant
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.update_tenant_request import UpdateTenantRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    update_tenant_request = UpdateTenantRequest(
        name="j",
        settings={
            "key": "key_example",
        },
    ) # UpdateTenantRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update(update_tenant_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_request** | [**UpdateTenantRequest**](UpdateTenantRequest.md)|  |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member**
> TenantMemberResponse update_member(member_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import tenants_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.update_tenant_member_request import UpdateTenantMemberRequest
from basistheory.model.tenant_member_response import TenantMemberResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.basistheory.com
# See configuration.py for a list of all supported configuration parameters.
configuration = basistheory.Configuration(
    host = "https://api.basistheory.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    member_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    update_tenant_member_request = UpdateTenantMemberRequest(
        role="role_example",
    ) # UpdateTenantMemberRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_member(member_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->update_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_member(member_id, update_tenant_member_request=update_tenant_member_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TenantsApi->update_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  |
 **update_tenant_member_request** | [**UpdateTenantMemberRequest**](UpdateTenantMemberRequest.md)|  | [optional]

### Return type

[**TenantMemberResponse**](TenantMemberResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

