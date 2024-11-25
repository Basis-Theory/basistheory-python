# basistheory.ApplicationTemplatesApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ApplicationTemplatesApi.md#get) | **GET** /application-templates | 
[**get_by_id**](ApplicationTemplatesApi.md#get_by_id) | **GET** /application-templates/{id} | 


# **get**
> [ApplicationTemplate] get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_templates_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application_template import ApplicationTemplate
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
    api_instance = application_templates_api.ApplicationTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationTemplatesApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ApplicationTemplate]**](ApplicationTemplate.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> ApplicationTemplate get_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import application_templates_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.application_template import ApplicationTemplate
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
    api_instance = application_templates_api.ApplicationTemplatesApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ApplicationTemplatesApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ApplicationTemplate**](ApplicationTemplate.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

