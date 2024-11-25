# basistheory.ReactorsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReactorsApi.md#create) | **POST** /reactors | 
[**delete**](ReactorsApi.md#delete) | **DELETE** /reactors/{id} | 
[**get**](ReactorsApi.md#get) | **GET** /reactors | 
[**get_by_id**](ReactorsApi.md#get_by_id) | **GET** /reactors/{id} | 
[**patch**](ReactorsApi.md#patch) | **PATCH** /reactors/{id} | 
[**react**](ReactorsApi.md#react) | **POST** /reactors/{id}/react | 
[**react_async**](ReactorsApi.md#react_async) | **POST** /reactors/{id}/react-async | 
[**result_get_by_id**](ReactorsApi.md#result_get_by_id) | **GET** /reactors/{id}/results/{requestId} | 
[**update**](ReactorsApi.md#update) | **PUT** /reactors/{id} | 


# **create**
> Reactor create(create_reactor_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.create_reactor_request import CreateReactorRequest
from basistheory.model.reactor import Reactor
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
    api_instance = reactors_api.ReactorsApi(api_client)
    create_reactor_request = CreateReactorRequest(
        name="j",
        code='''Aa6w77ikCX*cKCmv|`K/V''',
        application=Application(
            id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            tenant_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            name="j",
            key="S",
            keys=[
                ApplicationKey(
                    id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    key="key_example",
                    version="version_example",
                    created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            type="O",
            created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modified_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            modified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
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
        ),
        configuration={
            "key": "key_example",
        },
    ) # CreateReactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(create_reactor_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reactor_request** | [**CreateReactorRequest**](CreateReactorRequest.md)|  |

### Return type

[**Reactor**](Reactor.md)

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
from basistheory.api import reactors_api
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete(id)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->delete: %s\n" % e)
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
> ReactorPaginatedList get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.reactor_paginated_list import ReactorPaginatedList
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = [
        "62ECB020-8429-30cc-01FF-CCfeEe150AC3",
    ] # [str], none_type |  (optional)
    name = "j" # str, none_type |  (optional)
    page = 0 # int, none_type |  (optional)
    start = "start_example" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(id=id, name=name, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[str], none_type**|  | [optional]
 **name** | **str, none_type**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**ReactorPaginatedList**](ReactorPaginatedList.md)

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
> Reactor get_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.reactor import Reactor
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Reactor**](Reactor.md)

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

# **patch**
> patch(id, patch_reactor_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.patch_reactor_request import PatchReactorRequest
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    patch_reactor_request = PatchReactorRequest(
        name="j",
        application=Application(
            id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            tenant_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            name="j",
            key="S",
            keys=[
                ApplicationKey(
                    id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    key="key_example",
                    version="version_example",
                    created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            type="O",
            created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modified_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            modified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
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
        ),
        code='''Aa6w77ikCX*cKCmv|`K/V''',
        configuration={
            "key": "key_example",
        },
    ) # PatchReactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.patch(id, patch_reactor_request)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **patch_reactor_request** | [**PatchReactorRequest**](PatchReactorRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react**
> ReactResponse react(id, react_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.react_response import ReactResponse
from basistheory.model.react_request import ReactRequest
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    react_request = ReactRequest(
        args=None,
        callback_url="callback_url_example",
    ) # ReactRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.react(id, react_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->react: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **react_request** | [**ReactRequest**](ReactRequest.md)|  |

### Return type

[**ReactResponse**](ReactResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react_async**
> ReactResponse react_async(id, react_request_async)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.react_response import ReactResponse
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.react_request_async import ReactRequestAsync
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    react_request_async = ReactRequestAsync(
        args=None,
    ) # ReactRequestAsync | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.react_async(id, react_request_async)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->react_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **react_request_async** | [**ReactRequestAsync**](ReactRequestAsync.md)|  |

### Return type

[**ReactResponse**](ReactResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **result_get_by_id**
> bool, date, datetime, dict, float, int, list, str, none_type result_get_by_id(id, request_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    request_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.result_get_by_id(id, request_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->result_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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
> Reactor update(id, update_reactor_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactors_api
from basistheory.model.update_reactor_request import UpdateReactorRequest
from basistheory.model.reactor import Reactor
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
    api_instance = reactors_api.ReactorsApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    update_reactor_request = UpdateReactorRequest(
        name="j",
        application=Application(
            id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            tenant_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            name="j",
            key="S",
            keys=[
                ApplicationKey(
                    id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    key="key_example",
                    version="version_example",
                    created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            type="O",
            created_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modified_by="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
            modified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
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
        ),
        code='''Aa6w77ikCX*cKCmv|`K/V''',
        configuration={
            "key": "key_example",
        },
    ) # UpdateReactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update(id, update_reactor_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorsApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_reactor_request** | [**UpdateReactorRequest**](UpdateReactorRequest.md)|  |

### Return type

[**Reactor**](Reactor.md)

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

