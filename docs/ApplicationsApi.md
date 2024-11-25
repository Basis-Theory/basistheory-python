# basistheory.ApplicationsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ApplicationsApi.md#create) | **POST** /applications | 
[**delete**](ApplicationsApi.md#delete) | **DELETE** /applications/{id} | 
[**get**](ApplicationsApi.md#get) | **GET** /applications | 
[**get_by_id**](ApplicationsApi.md#get_by_id) | **GET** /applications/{id} | 
[**get_by_key**](ApplicationsApi.md#get_by_key) | **GET** /applications/key | 
[**regenerate_key**](ApplicationsApi.md#regenerate_key) | **POST** /applications/{id}/regenerate | 
[**update**](ApplicationsApi.md#update) | **PUT** /applications/{id} | 


# **create**
> Application create(create_application_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.create_application_request import CreateApplicationRequest
from basistheory.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    create_application_request = CreateApplicationRequest(
        name="j",
        type="O",
        expires_at="expires_at_example",
        permissions=[
            "permissions_example",
        ],
        rules=[
            AccessRule(
                description="description_example",
                priority=1,
                container="container_example",
                transform="transform_example",
                conditions=[
                    Condition(
                        attribute="attribute_example",
                        operator="operator_example",
                        value="value_example",
                    ),
                ],
                permissions=[
                    "permissions_example",
                ],
            ),
        ],
        create_key=True,
    ) # CreateApplicationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(create_application_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  |

### Return type

[**Application**](Application.md)

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
> delete(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete(id)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **get**
> ApplicationPaginatedList get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.application_paginated_list import ApplicationPaginatedList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    id = [
        "62ECB020-8429-30cc-01FF-CCfeEe150AC3",
    ] # [str], none_type |  (optional)
    type = [
        "type_example",
    ] # [str], none_type |  (optional)
    page = 0 # int, none_type |  (optional)
    start = "start_example" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(id=id, type=type, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[str], none_type**|  | [optional]
 **type** | **[str], none_type**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**ApplicationPaginatedList**](ApplicationPaginatedList.md)

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

# **get_by_id**
> Application get_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Application**](Application.md)

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

# **get_by_key**
> Application get_by_key()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_by_key()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->get_by_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Application**](Application.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_key**
> Application regenerate_key(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.regenerate_key(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->regenerate_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Application**](Application.md)

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
**422** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Application update(id, update_application_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import applications_api
from basistheory.model.update_application_request import UpdateApplicationRequest
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application import Application
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
    api_instance = applications_api.ApplicationsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    update_application_request = UpdateApplicationRequest(
        name="j",
        permissions=[
            "permissions_example",
        ],
        rules=[
            AccessRule(
                description="description_example",
                priority=1,
                container="container_example",
                transform="transform_example",
                conditions=[
                    Condition(
                        attribute="attribute_example",
                        operator="operator_example",
                        value="value_example",
                    ),
                ],
                permissions=[
                    "permissions_example",
                ],
            ),
        ],
    ) # UpdateApplicationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update(id, update_application_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_application_request** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  |

### Return type

[**Application**](Application.md)

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

