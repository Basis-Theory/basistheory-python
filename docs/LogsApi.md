# basistheory.LogsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](LogsApi.md#get) | **GET** /logs | 
[**get_entity_types**](LogsApi.md#get_entity_types) | **GET** /logs/entity-types | 


# **get**
> LogPaginatedList get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import logs_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.log_paginated_list import LogPaginatedList
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
    api_instance = logs_api.LogsApi(api_client)
    entity_type = "O" # str, none_type |  (optional)
    entity_id = "j" # str, none_type |  (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type |  (optional)
    page = 1 # int, none_type |  (optional)
    start = "j" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(entity_type=entity_type, entity_id=entity_id, start_date=start_date, end_date=end_date, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling LogsApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str, none_type**|  | [optional]
 **entity_id** | **str, none_type**|  | [optional]
 **start_date** | **datetime, none_type**|  | [optional]
 **end_date** | **datetime, none_type**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**LogPaginatedList**](LogPaginatedList.md)

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

# **get_entity_types**
> [LogEntityType] get_entity_types()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import logs_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.log_entity_type import LogEntityType
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
    api_instance = logs_api.LogsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_entity_types()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling LogsApi->get_entity_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LogEntityType]**](LogEntityType.md)

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

