"""
    BasisTheory Vault API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from basistheory.api_client import ApiClient, Endpoint as _Endpoint
from basistheory.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
    set_request_options
)
from basistheory.model.basis_theory_error import BasisTheoryError
from basistheory.model.paginated_token_list import PaginatedTokenList
from basistheory.model.token import Token


class TokensApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_endpoint = _Endpoint(
            settings={
                'response_type': (Token,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'token',
                    'request_options'
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'token':
                        (Token,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'token': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens/{id}',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Token,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens/{id}',
                'operation_id': 'get_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'children',
                    'children_type',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'children':
                        (bool,),
                    'children_type':
                        ([str],),
                },
                'attribute_map': {
                    'id': 'id',
                    'children': 'children',
                    'children_type': 'children_type',
                },
                'location_map': {
                    'id': 'path',
                    'children': 'query',
                    'children_type': 'query',
                },
                'collection_format_map': {
                    'children_type': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_decrypted_endpoint = _Endpoint(
            settings={
                'response_type': (Token,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens/{id}/decrypt',
                'operation_id': 'get_decrypted',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'children',
                    'children_type',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'children':
                        (bool,),
                    'children_type':
                        ([str],),
                },
                'attribute_map': {
                    'id': 'id',
                    'children': 'children',
                    'children_type': 'children_type',
                },
                'location_map': {
                    'id': 'path',
                    'children': 'query',
                    'children_type': 'query',
                },
                'collection_format_map': {
                    'children_type': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_endpoint = _Endpoint(
            settings={
                'response_type': (PaginatedTokenList,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'type',
                    'metadata',
                    'page',
                    'size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        ([str],),
                    'type':
                        ([str],),
                    'metadata':
                        ({str: (str,)},),
                    'page':
                        (int,),
                    'size':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'type': 'type',
                    'metadata': 'metadata',
                    'page': 'page',
                    'size': 'size',
                },
                'location_map': {
                    'id': 'query',
                    'type': 'query',
                    'metadata': 'query',
                    'page': 'query',
                    'size': 'query',
                },
                'collection_format_map': {
                    'id': 'multi',
                    'type': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_decrypted_endpoint = _Endpoint(
            settings={
                'response_type': (PaginatedTokenList,),
                'auth': [
                    'apiKey'
                ],
                'endpoint_path': '/tokens/decrypt',
                'operation_id': 'list_decrypted',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'children',
                    'children_type',
                    'decrypt_type',
                    'page',
                    'size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        ([str],),
                    'children':
                        (bool,),
                    'children_type':
                        ([str],),
                    'decrypt_type':
                        ([str],),
                    'page':
                        (int,),
                    'size':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'children': 'children',
                    'children_type': 'children_type',
                    'decrypt_type': 'decrypt_type',
                    'page': 'page',
                    'size': 'size',
                },
                'location_map': {
                    'id': 'query',
                    'children': 'query',
                    'children_type': 'query',
                    'decrypt_type': 'query',
                    'page': 'query',
                    'size': 'query',
                },
                'collection_format_map': {
                    'id': 'multi',
                    'children_type': 'multi',
                    'decrypt_type': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create(
        self,
        token,
        **kwargs,
    ):
        """create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()

        Args:
            token (Token): token to create

        Keyword Args:
            request_options(RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Token
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['token'] = \
            token
        return self.create_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        id,
        **kwargs
    ):
        """delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): id for the token to delete

        Keyword Args:
            request_options(RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def get_by_id(
        self,
        id,
        **kwargs
    ):
        """get_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): id for the token

        Keyword Args:
            children (bool): [optional]
            children_type ([str]): [optional]
            request_options(RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Token
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_by_id_endpoint.call_with_http_info(**kwargs)

    def get_decrypted(
        self,
        id,
        **kwargs
    ):
        """get_decrypted  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_decrypted(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): id for the token

        Keyword Args:
            children (bool): [optional]
            children_type ([str]): [optional]
            request_options (RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Token
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_decrypted_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs,
    ):
        """list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            id ([str]): [optional]
            type ([str]): [optional]
            metadata ({str: (str,)}): [optional]
            page (int): [optional]
            size (int): [optional]
            request_options(RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PaginatedTokenList
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_endpoint.call_with_http_info(**kwargs)

    def list_decrypted(
        self,
        **kwargs
    ):
        """list_decrypted  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_decrypted(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            id ([str]): [optional]
            children (bool): [optional]
            children_type ([str]): [optional]
            decrypt_type ([str]): [optional]
            page (int): [optional]
            size (int): [optional]
            request_options(RequestOptions): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PaginatedTokenList
                If the method is called asynchronously, returns the request
                thread.
        """
        if kwargs.get('request_options'):
            set_request_options(kwargs.pop('request_options'), self)

        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_decrypted_endpoint.call_with_http_info(**kwargs)

