# basistheory.ApplicationKeysApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ApplicationKeysApi.md#create) | **POST** /applications/{id}/keys | 
[**delete**](ApplicationKeysApi.md#delete) | **DELETE** /applications/{id}/keys/{keyId} | 
[**get**](ApplicationKeysApi.md#get) | **GET** /applications/{id}/keys | 
[**get_by_id**](ApplicationKeysApi.md#get_by_id) | **GET** /applications/{id}/keys/{keyId} | 


# **create**
> ApplicationKey create(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_keys_api
from basistheory.model.application_key import ApplicationKey
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
    api_instance = application_keys_api.ApplicationKeysApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationKeysApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ApplicationKey**](ApplicationKey.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id, key_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_keys_api
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
    api_instance = application_keys_api.ApplicationKeysApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    key_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete(id, key_id)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationKeysApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **key_id** | **str**|  |

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

# **get**
> [ApplicationKey] get(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_keys_api
from basistheory.model.application_key import ApplicationKey
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
    api_instance = application_keys_api.ApplicationKeysApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    id2 = [
        "62ECB020-8429-30cc-01FF-CCfeEe150AC3",
    ] # [str] |  (optional)
    type = [
        "type_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationKeysApi->get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(id, id2=id2, type=type)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationKeysApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id2** | **[str]**|  | [optional]
 **type** | **[str]**|  | [optional]

### Return type

[**[ApplicationKey]**](ApplicationKey.md)

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
> ApplicationKey get_by_id(id, key_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_keys_api
from basistheory.model.application_key import ApplicationKey
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
    api_instance = application_keys_api.ApplicationKeysApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    key_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id, key_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationKeysApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **key_id** | **str**|  |

### Return type

[**ApplicationKey**](ApplicationKey.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

