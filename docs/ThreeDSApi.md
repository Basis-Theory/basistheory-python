# basistheory.ThreeDSApi

All URIs are relative to *https://api.basistheory.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**three_ds_authenticate_session**](ThreeDSApi.md#three_ds_authenticate_session) | **POST** /3ds/sessions/{sessionId}/authenticate | 
[**three_ds_create_session**](ThreeDSApi.md#three_ds_create_session) | **POST** /3ds/sessions | 
[**three_ds_get_challenge_result**](ThreeDSApi.md#three_ds_get_challenge_result) | **GET** /3ds/sessions/{sessionId}/challenge-result | 
[**three_ds_get_session_by_id**](ThreeDSApi.md#three_ds_get_session_by_id) | **GET** /3ds/sessions/{id} | 


# **three_ds_authenticate_session**
> ThreeDSAuthentication three_ds_authenticate_session(session_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import three_ds_api
from basistheory.model.authenticate_three_ds_session_request import AuthenticateThreeDSSessionRequest
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.three_ds_authentication import ThreeDSAuthentication
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
    api_instance = three_ds_api.ThreeDSApi(api_client)
    session_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 
    authenticate_three_ds_session_request = AuthenticateThreeDSSessionRequest(
        authentication_category="authentication_category_example",
        authentication_type="authentication_type_example",
        challenge_preference="challenge_preference_example",
        request_decoupled_challenge=True,
        decoupled_challenge_max_time=1,
        purchase_info=ThreeDSPurchaseInfo(
            amount="amount_example",
            currency="currency_example",
            exponent="exponent_example",
            date="date_example",
            transaction_type="transaction_type_example",
            installment_count="installment_count_example",
            recurring_expiration="recurring_expiration_example",
            recurring_frequency="recurring_frequency_example",
        ),
        merchant_info=ThreeDSMerchantInfo(
            mid="mid_example",
            acquirer_bin="acquirer_bin_example",
            name="name_example",
            country_code="country_code_example",
            category_code="category_code_example",
            risk_info=ThreeDSMerchantRiskInfo(
                delivery_email="delivery_email_example",
                delivery_time_frame="delivery_time_frame_example",
                gift_card_amount="gift_card_amount_example",
                gift_card_count="gift_card_count_example",
                gift_card_currency="gift_card_currency_example",
                pre_order_purchase=True,
                pre_order_date="pre_order_date_example",
                reordered_purchase=True,
                shipping_method="shipping_method_example",
            ),
        ),
        requestor_info=ThreeDSRequestorInfo(
            id="id_example",
            name="name_example",
            url="url_example",
        ),
        cardholder_info=ThreeDSCardholderInfo(
            account_id="account_id_example",
            account_type="account_type_example",
            account_info=ThreeDSCardholderAccountInfo(
                account_age="account_age_example",
                account_last_changed="account_last_changed_example",
                account_change_date="account_change_date_example",
                account_created_date="account_created_date_example",
                account_pwd_last_changed="account_pwd_last_changed_example",
                account_pwd_change_date="account_pwd_change_date_example",
                purchase_count_half_year="purchase_count_half_year_example",
                transaction_count_day="transaction_count_day_example",
                payment_account_age="payment_account_age_example",
                transaction_count_year="transaction_count_year_example",
                payment_account_created="payment_account_created_example",
                shipping_address_first_used="shipping_address_first_used_example",
                shipping_address_usage_date="shipping_address_usage_date_example",
                shipping_account_name_match=True,
                suspicious_activity_observed=True,
            ),
            authentication_info=ThreeDSCardholderAuthenticationInfo(
                method="method_example",
                timestamp="timestamp_example",
                data="data_example",
            ),
            prior_authentication_info=ThreeDSPriorAuthenticationInfo(
                method="method_example",
                timestamp="timestamp_example",
                reference_id="reference_id_example",
                data="data_example",
            ),
            name="name_example",
            email="email_example",
            phone_number=ThreeDSCardholderPhoneNumber(
                country_code="country_code_example",
                number="number_example",
            ),
            mobile_phone_number=ThreeDSCardholderPhoneNumber(
                country_code="country_code_example",
                number="number_example",
            ),
            work_phone_number=ThreeDSCardholderPhoneNumber(
                country_code="country_code_example",
                number="number_example",
            ),
            billing_shipping_address_match="billing_shipping_address_match_example",
            billing_address=ThreeDSAddress(
                line1="line1_example",
                line2="line2_example",
                line3="line3_example",
                postal_code="postal_code_example",
                city="city_example",
                state_code="state_code_example",
                country_code="country_code_example",
            ),
            shipping_address=ThreeDSAddress(
                line1="line1_example",
                line2="line2_example",
                line3="line3_example",
                postal_code="postal_code_example",
                city="city_example",
                state_code="state_code_example",
                country_code="country_code_example",
            ),
        ),
        broadcast_info=None,
        message_extensions=[
            ThreeDSMessageExtension(
                id="id_example",
                name="name_example",
                critical=True,
                data=None,
            ),
        ],
    ) # AuthenticateThreeDSSessionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.three_ds_authenticate_session(session_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ThreeDSApi->three_ds_authenticate_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.three_ds_authenticate_session(session_id, authenticate_three_ds_session_request=authenticate_three_ds_session_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ThreeDSApi->three_ds_authenticate_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |
 **authenticate_three_ds_session_request** | [**AuthenticateThreeDSSessionRequest**](AuthenticateThreeDSSessionRequest.md)|  | [optional]

### Return type

[**ThreeDSAuthentication**](ThreeDSAuthentication.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **three_ds_create_session**
> CreateThreeDSSessionResponse three_ds_create_session()



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import three_ds_api
from basistheory.model.create_three_ds_session_request import CreateThreeDSSessionRequest
from basistheory.model.create_three_ds_session_response import CreateThreeDSSessionResponse
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
    api_instance = three_ds_api.ThreeDSApi(api_client)
    create_three_ds_session_request = CreateThreeDSSessionRequest(
        pan="pan_example",
        token_id="token_id_example",
        token_intent_id="token_intent_id_example",
        type="type_example",
        device="device_example",
        device_info=ThreeDSDeviceInfo(
            browser_accept_header="browser_accept_header_example",
            browser_ip="browser_ip_example",
            browser_javascript_enabled=True,
            browser_java_enabled=True,
            browser_language="browser_language_example",
            browser_color_depth="browser_color_depth_example",
            browser_screen_height="browser_screen_height_example",
            browser_screen_width="browser_screen_width_example",
            browser_tz="browser_tz_example",
            browser_user_agent="browser_user_agent_example",
            sdk_transaction_id="sdk_transaction_id_example",
            sdk_application_id="sdk_application_id_example",
            sdk_encryption_data="sdk_encryption_data_example",
            sdk_ephemeral_public_key="sdk_ephemeral_public_key_example",
            sdk_max_timeout="sdk_max_timeout_example",
            sdk_reference_number="sdk_reference_number_example",
            sdk_render_options=ThreeDSMobileSdkRenderOptions(
                sdk_interface="sdk_interface_example",
                sdk_ui_type=[
                    "sdk_ui_type_example",
                ],
            ),
        ),
    ) # CreateThreeDSSessionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.three_ds_create_session(create_three_ds_session_request=create_three_ds_session_request)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ThreeDSApi->three_ds_create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_three_ds_session_request** | [**CreateThreeDSSessionRequest**](CreateThreeDSSessionRequest.md)|  | [optional]

### Return type

[**CreateThreeDSSessionResponse**](CreateThreeDSSessionResponse.md)

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

# **three_ds_get_challenge_result**
> ThreeDSAuthentication three_ds_get_challenge_result(session_id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import three_ds_api
from basistheory.model.problem_details import ProblemDetails
from basistheory.model.three_ds_authentication import ThreeDSAuthentication
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
    api_instance = three_ds_api.ThreeDSApi(api_client)
    session_id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.three_ds_get_challenge_result(session_id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ThreeDSApi->three_ds_get_challenge_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |

### Return type

[**ThreeDSAuthentication**](ThreeDSAuthentication.md)

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

# **three_ds_get_session_by_id**
> ThreeDSSession three_ds_get_session_by_id(id)



### Example

* Api Key Authentication (ApiKey):

```python
import time
import basistheory
from basistheory.api import three_ds_api
from basistheory.model.three_ds_session import ThreeDSSession
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
    api_instance = three_ds_api.ThreeDSApi(api_client)
    id = "62ECB020-8429-30cc-01FF-CCfeEe150AC3" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.three_ds_get_session_by_id(id)
        pprint(api_response)
    except basistheory.ApiException as e:
        print("Exception when calling ThreeDSApi->three_ds_get_session_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ThreeDSSession**](ThreeDSSession.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

