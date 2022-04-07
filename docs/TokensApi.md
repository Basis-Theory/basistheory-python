# Token Client

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TokensApi.md#create) | **POST** /tokens | Create a new token for the Tenant.
[**delete**](TokensApi.md#delete) | **DELETE** /tokens/{id} | Delete a token by ID in the Tenant.
[**get_by_id**](TokensApi.md#get_by_id) | **GET** /tokens/{id} | Get a token by ID in the Tenant.
[**list**](TokensApi.md#list) | **GET** /tokens | Get a list of tokens for the Tenant.

# **create**

> Token create()

### Example

```python
import basistheory
from basistheory.api import tokens_api
from basistheory.model.token import Token
from pprint import pprint

# Set client wide api key
configuration = basistheory.Configuration(
    api_key = "API KEY"
)

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the token client
    token_client = tokens_api.TokensApi(api_client)

    token = Token(type="token", data="my data", metadata={"nonSensitiveField": "Non-Sensitive Value"})

    try:
        api_response = token_client.create(token=token)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TokensApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description
------------- | ------------- | -------------
 **token** | [**Token**](Token.md)|

### Return type

[**Token**](Token.md)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description
|-------------|-------------
**201** | Success |
**400** | Bad Request |
**401** | Unauthorized |
**403** | Forbidden |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

### Example

```python
import basistheory
from basistheory.api import tokens_api
from pprint import pprint

# Set client wide api key
configuration = basistheory.Configuration(
    api_key = "API KEY"
)

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the token client
    token_client = tokens_api.TokensApi(api_client)

    id = "c06d0789-0a38-40be-b7cc-c28a718f76f1"

    try:
        api_response = token_client.delete(id=id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TokensApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  
------------- | ------------- | -------------
 **id** | **str**|

### Return type

void (empty response body)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description
|-------------|-------------
**204** | Success |
**400** | Bad Request |
**401** | Unauthorized |
**403** | Forbidden |
**404** | Not Found |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> Token get_by_id(id)

### Example

```python
import basistheory
from basistheory.api import tokens_api
from pprint import pprint

# Set client wide api key
configuration = basistheory.Configuration(
    api_key = "API KEY"
)

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the token client
    token_client = tokens_api.TokensApi(api_client)

    id = "c06d0789-0a38-40be-b7cc-c28a718f76f1"

    try:
        api_response = token_client.get_by_id(id=id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TokensApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description
------------- | ------------- | -------------
 **id** | **str**|
 **children** | **bool**|
 **children_type** | **[str]**|

### Return type

[**Token**](Token.md)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details

| Status code | Description
|-------------|-------------
**200** | Success |
**401** | Unauthorized |
**403** | Forbidden |
**404** | Not Found |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedTokenList list()

### Example

```python
import basistheory
from basistheory.api import tokens_api
from pprint import pprint

# Set client wide api key
configuration = basistheory.Configuration(
    api_key = "API KEY"
)

# Enter a context with an instance of the API client
with basistheory.ApiClient(configuration) as api_client:
    # Create an instance of the token client
    token_client = tokens_api.TokensApi(api_client)

    try:
        api_response = token_client.list()
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling TokensApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description
------------- | ------------- | -------------
 **id** | **[str]**|
 **type** | **[str]**|
 **metadata** | **{str: (str,)}**|
 **page** | **int**|
 **size** | **int**|

### Return type

[**PaginatedTokenList**](PaginatedTokenList.md)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description
|-------------|-------------
**200** | Success |
**401** | Unauthorized |
**403** | Forbidden |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)