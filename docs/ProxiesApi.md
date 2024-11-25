# basistheory.ProxiesApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ProxiesApi.md#create) | **POST** /proxies | 
[**delete**](ProxiesApi.md#delete) | **DELETE** /proxies/{id} | 
[**get**](ProxiesApi.md#get) | **GET** /proxies | 
[**get_by_id**](ProxiesApi.md#get_by_id) | **GET** /proxies/{id} | 
[**patch**](ProxiesApi.md#patch) | **PATCH** /proxies/{id} | 
[**update**](ProxiesApi.md#update) | **PUT** /proxies/{id} | 


# **create**
> Proxy create(create_proxy_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import proxies_api
from basistheory.model.proxy import Proxy
from basistheory.model.create_proxy_request import CreateProxyRequest
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
    api_instance = proxies_api.ProxiesApi(api_client)
    create_proxy_request = CreateProxyRequest(
        name="j",
        destination_url="https://j",
        request_reactor_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
        response_reactor_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
        request_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
        response_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
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
        require_auth=True,
    ) # CreateProxyRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(create_proxy_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ProxiesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_proxy_request** | [**CreateProxyRequest**](CreateProxyRequest.md)|  |

### Return type

[**Proxy**](Proxy.md)

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
from basistheory.api import proxies_api
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
    api_instance = proxies_api.ProxiesApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete(id)
    except basistheory.ApiException as e:
        print("Exception when calling ProxiesApi->delete: %s\n" % e)
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
> ProxyPaginatedList get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import proxies_api
from basistheory.model.proxy_paginated_list import ProxyPaginatedList
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
    api_instance = proxies_api.ProxiesApi(api_client)
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
        print("Exception when calling ProxiesApi->get: %s\n" % e)
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

[**ProxyPaginatedList**](ProxyPaginatedList.md)

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
> Proxy get_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import proxies_api
from basistheory.model.proxy import Proxy
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
    api_instance = proxies_api.ProxiesApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ProxiesApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Proxy**](Proxy.md)

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
> patch(id, patch_proxy_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import proxies_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.patch_proxy_request import PatchProxyRequest
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
    api_instance = proxies_api.ProxiesApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    patch_proxy_request = PatchProxyRequest(
        name="j",
        destination_url="destination_url_example",
        request_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
        response_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
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
        require_auth=True,
    ) # PatchProxyRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.patch(id, patch_proxy_request)
    except basistheory.ApiException as e:
        print("Exception when calling ProxiesApi->patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **patch_proxy_request** | [**PatchProxyRequest**](PatchProxyRequest.md)|  |

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

# **update**
> Proxy update(id, update_proxy_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import proxies_api
from basistheory.model.update_proxy_request import UpdateProxyRequest
from basistheory.model.proxy import Proxy
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
    api_instance = proxies_api.ProxiesApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    update_proxy_request = UpdateProxyRequest(
        name="j",
        destination_url="https://j",
        request_reactor_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
        response_reactor_id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
        request_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
        response_transform=ProxyTransform(
            type="type_example",
            code="code_example",
            matcher="matcher_example",
            expression="expression_example",
            replacement="replacement_example",
        ),
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
        require_auth=True,
    ) # UpdateProxyRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update(id, update_proxy_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ProxiesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_proxy_request** | [**UpdateProxyRequest**](UpdateProxyRequest.md)|  |

### Return type

[**Proxy**](Proxy.md)

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

