# basistheory.SessionsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](SessionsApi.md#authorize) | **POST** /sessions/authorize | 
[**create**](SessionsApi.md#create) | **POST** /sessions | 


# **authorize**
> authorize(authorize_session_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import sessions_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.authorize_session_request import AuthorizeSessionRequest
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
    api_instance = sessions_api.SessionsApi(api_client)
    authorize_session_request = AuthorizeSessionRequest(
        nonce="nonce_example",
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
    ) # AuthorizeSessionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.authorize(authorize_session_request)
    except basistheory.ApiException as e:
        print("Exception when calling SessionsApi->authorize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_session_request** | [**AuthorizeSessionRequest**](AuthorizeSessionRequest.md)|  |

### Return type

void (empty response body)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> CreateSessionResponse create()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import sessions_api
from basistheory.model.create_session_response import CreateSessionResponse
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
    api_instance = sessions_api.SessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.create()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling SessionsApi->create: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

