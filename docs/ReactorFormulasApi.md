# basistheory.ReactorFormulasApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReactorFormulasApi.md#create) | **POST** /reactor-formulas | 
[**delete**](ReactorFormulasApi.md#delete) | **DELETE** /reactor-formulas/{id} | 
[**get**](ReactorFormulasApi.md#get) | **GET** /reactor-formulas | 
[**get_by_id**](ReactorFormulasApi.md#get_by_id) | **GET** /reactor-formulas/{id} | 
[**update**](ReactorFormulasApi.md#update) | **PUT** /reactor-formulas/{id} | 


# **create**
> ReactorFormula create(create_reactor_formula_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactor_formulas_api
from basistheory.model.reactor_formula import ReactorFormula
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.create_reactor_formula_request import CreateReactorFormulaRequest
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
    api_instance = reactor_formulas_api.ReactorFormulasApi(api_client)
    create_reactor_formula_request = CreateReactorFormulaRequest(
        id="62ECB020-8429-30cc-01FF-CCfeEe150AC3",
        type="official",
        name="j",
        description='''Aa6w77ikCX*cKCmv|`K/V''',
        icon="icon_example",
        code="code_example",
        configuration=[
            ReactorFormulaConfiguration(
                name="z",
                description="jUR,rZ#UM/?R,Fp^l6$ARj",
                type="number",
            ),
        ],
        request_parameters=[
            ReactorFormulaRequestParameter(
                name="SG]PAyG[8g.D_[qU9n7GSHc0slDgSk",
                description="jUR,rZ#UM/?R,Fp^l6$ARj",
                type="number",
                optional=True,
            ),
        ],
    ) # CreateReactorFormulaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create(create_reactor_formula_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorFormulasApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reactor_formula_request** | [**CreateReactorFormulaRequest**](CreateReactorFormulaRequest.md)|  |

### Return type

[**ReactorFormula**](ReactorFormula.md)

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
from basistheory.api import reactor_formulas_api
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
    api_instance = reactor_formulas_api.ReactorFormulasApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete(id)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorFormulasApi->delete: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ReactorFormulaPaginatedList get()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactor_formulas_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.reactor_formula_paginated_list import ReactorFormulaPaginatedList
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
    api_instance = reactor_formulas_api.ReactorFormulasApi(api_client)
    name = "j" # str, none_type |  (optional)
    page = 0 # int, none_type |  (optional)
    start = "start_example" # str, none_type |  (optional)
    size = 0 # int, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get(name=name, page=page, start=start, size=size)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorFormulasApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str, none_type**|  | [optional]
 **page** | **int, none_type**|  | [optional]
 **start** | **str, none_type**|  | [optional]
 **size** | **int, none_type**|  | [optional]

### Return type

[**ReactorFormulaPaginatedList**](ReactorFormulaPaginatedList.md)

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

# **get_by_id**
> ReactorFormula get_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactor_formulas_api
from basistheory.model.reactor_formula import ReactorFormula
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
    api_instance = reactor_formulas_api.ReactorFormulasApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorFormulasApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ReactorFormula**](ReactorFormula.md)

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

# **update**
> ReactorFormula update(id, update_reactor_formula_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import reactor_formulas_api
from basistheory.model.reactor_formula import ReactorFormula
from basistheory.model.update_reactor_formula_request import UpdateReactorFormulaRequest
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
    api_instance = reactor_formulas_api.ReactorFormulasApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    update_reactor_formula_request = UpdateReactorFormulaRequest(
        type="official",
        name="j",
        description='''Aa6w77ikCX*cKCmv|`K/V''',
        icon="icon_example",
        code='''Aa6w77ikCX*cKCmv|`K/V''',
        configuration=[
            ReactorFormulaConfiguration(
                name="z",
                description="jUR,rZ#UM/?R,Fp^l6$ARj",
                type="number",
            ),
        ],
        request_parameters=[
            ReactorFormulaRequestParameter(
                name="SG]PAyG[8g.D_[qU9n7GSHc0slDgSk",
                description="jUR,rZ#UM/?R,Fp^l6$ARj",
                type="number",
                optional=True,
            ),
        ],
    ) # UpdateReactorFormulaRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update(id, update_reactor_formula_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ReactorFormulasApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **update_reactor_formula_request** | [**UpdateReactorFormulaRequest**](UpdateReactorFormulaRequest.md)|  |

### Return type

[**ReactorFormula**](ReactorFormula.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

