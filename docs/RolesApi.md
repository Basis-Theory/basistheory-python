# basistheory.RolesApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](RolesApi.md#get) | **GET** /roles | 


# **get**
> [Role] get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import roles_api
from basistheory.model.role import Role
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
    api_instance = roles_api.RolesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling RolesApi->get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Role]**](Role.md)

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

