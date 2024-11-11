"""
    Basis Theory API

    ## Getting Started * Sign-in to [Basis Theory](https://basistheory.com) and go to [Applications](https://portal.basistheory.com/applications) * Create a Basis Theory Private Application * All permissions should be selected * Paste the API Key into the `BT-API-KEY` variable  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from basistheory.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from basistheory.exceptions import ApiAttributeError


def lazy_import():
    from basistheory.model.three_ds_cardholder_info import ThreeDSCardholderInfo
    from basistheory.model.three_ds_merchant_info import ThreeDSMerchantInfo
    from basistheory.model.three_ds_message_extension import ThreeDSMessageExtension
    from basistheory.model.three_ds_purchase_info import ThreeDSPurchaseInfo
    from basistheory.model.three_ds_requestor_info import ThreeDSRequestorInfo
    globals()['ThreeDSCardholderInfo'] = ThreeDSCardholderInfo
    globals()['ThreeDSMerchantInfo'] = ThreeDSMerchantInfo
    globals()['ThreeDSMessageExtension'] = ThreeDSMessageExtension
    globals()['ThreeDSPurchaseInfo'] = ThreeDSPurchaseInfo
    globals()['ThreeDSRequestorInfo'] = ThreeDSRequestorInfo


class AuthenticateThreeDSSessionRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('authentication_category',): {
            'min_length': 1,
        },
        ('authentication_type',): {
            'min_length': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'authentication_category': (str,),  # noqa: E501
            'authentication_type': (str,),  # noqa: E501
            'requestor_info': (ThreeDSRequestorInfo,),  # noqa: E501
            'challenge_preference': (str, none_type,),  # noqa: E501
            'request_decoupled_challenge': (bool,),  # noqa: E501
            'decoupled_challenge_max_time': (int, none_type,),  # noqa: E501
            'purchase_info': (ThreeDSPurchaseInfo,),  # noqa: E501
            'merchant_info': (ThreeDSMerchantInfo,),  # noqa: E501
            'cardholder_info': (ThreeDSCardholderInfo,),  # noqa: E501
            'broadcast_info': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'message_extensions': ([ThreeDSMessageExtension], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'authentication_category': 'authentication_category',  # noqa: E501
        'authentication_type': 'authentication_type',  # noqa: E501
        'requestor_info': 'requestor_info',  # noqa: E501
        'challenge_preference': 'challenge_preference',  # noqa: E501
        'request_decoupled_challenge': 'request_decoupled_challenge',  # noqa: E501
        'decoupled_challenge_max_time': 'decoupled_challenge_max_time',  # noqa: E501
        'purchase_info': 'purchase_info',  # noqa: E501
        'merchant_info': 'merchant_info',  # noqa: E501
        'cardholder_info': 'cardholder_info',  # noqa: E501
        'broadcast_info': 'broadcast_info',  # noqa: E501
        'message_extensions': 'message_extensions',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, authentication_category, authentication_type, requestor_info, *args, **kwargs):  # noqa: E501
        """AuthenticateThreeDSSessionRequest - a model defined in OpenAPI

        Args:
            authentication_category (str):
            authentication_type (str):
            requestor_info (ThreeDSRequestorInfo):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            challenge_preference (str, none_type): [optional]  # noqa: E501
            request_decoupled_challenge (bool): [optional]  # noqa: E501
            decoupled_challenge_max_time (int, none_type): [optional]  # noqa: E501
            purchase_info (ThreeDSPurchaseInfo): [optional]  # noqa: E501
            merchant_info (ThreeDSMerchantInfo): [optional]  # noqa: E501
            cardholder_info (ThreeDSCardholderInfo): [optional]  # noqa: E501
            broadcast_info (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            message_extensions ([ThreeDSMessageExtension], none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.authentication_category = authentication_category
        self.authentication_type = authentication_type
        self.requestor_info = requestor_info
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, authentication_category, authentication_type, requestor_info, *args, **kwargs):  # noqa: E501
        """AuthenticateThreeDSSessionRequest - a model defined in OpenAPI

        Args:
            authentication_category (str):
            authentication_type (str):
            requestor_info (ThreeDSRequestorInfo):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            challenge_preference (str, none_type): [optional]  # noqa: E501
            request_decoupled_challenge (bool): [optional]  # noqa: E501
            decoupled_challenge_max_time (int, none_type): [optional]  # noqa: E501
            purchase_info (ThreeDSPurchaseInfo): [optional]  # noqa: E501
            merchant_info (ThreeDSMerchantInfo): [optional]  # noqa: E501
            cardholder_info (ThreeDSCardholderInfo): [optional]  # noqa: E501
            broadcast_info (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            message_extensions ([ThreeDSMessageExtension], none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.authentication_category = authentication_category
        self.authentication_type = authentication_type
        self.requestor_info = requestor_info
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
