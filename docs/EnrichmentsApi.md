# basistheory.EnrichmentsApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_account_verify**](EnrichmentsApi.md#bank_account_verify) | **POST** /enrichments/bank-account-verify | 


# **bank_account_verify**
> bank_account_verify(bank_verification_request)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import enrichments_api
from basistheory.model.validation_problem_details import ValidationProblemDetails
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.bank_verification_request import BankVerificationRequest
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
    api_instance = enrichments_api.EnrichmentsApi(api_client)
    bank_verification_request = BankVerificationRequest(
        token_id="token_id_example",
        country_code="country_code_example",
        routing_number="routing_number_example",
    ) # BankVerificationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.bank_account_verify(bank_verification_request)
    except basistheory.ApiException as e:
        print("Exception when calling EnrichmentsApi->bank_account_verify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_verification_request** | [**BankVerificationRequest**](BankVerificationRequest.md)|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

