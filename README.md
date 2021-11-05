# Basis Theory Python SDK

The [Basis Theory](https://basistheory.com/) Python SDK for Python >=3.7

:warning: **This SDK is currently in alpha state and is subject to changes.**

## Installation

### pip install

From the git repository

```sh
pip install git+https://github.com/Basis-Theory/basistheory-python.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Basis-Theory/basistheory-python.git`)

Then import the package:

```python
import basistheory
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import basistheory
```

## Documentation

:warning: **Documentation is currently in alpha and is subject to changes.**<br>
If you need any assistance, please contact support@basistheory.com at this time.

### Client Methods

All URIs are relative to *https://api.basistheory.com*

Class | Method | HTTP request
------------ | ------------- | -------------
*TokensApi* | [**create**](docs/TokensApi.md#create) | **POST** /tokens
*TokensApi* | [**delete**](docs/TokensApi.md#delete) | **DELETE** /tokens/{id}
*TokensApi* | [**get_by_id**](docs/TokensApi.md#get_by_id) | **GET** /tokens/{id}
*TokensApi* | [**get_decrypted**](docs/TokensApi.md#get_decrypted) | **GET** /tokens/{id}/decrypt
*TokensApi* | [**list**](docs/TokensApi.md#list) | **GET** /tokens
*TokensApi* | [**list_decrypted**](docs/TokensApi.md#list_decrypted) | **GET** /tokens/decrypt

### Models

- [EncryptionKey](docs/EncryptionKey.md)
- [EncryptionMetadata](docs/EncryptionMetadata.md)
- [PaginatedTokenList](docs/PaginatedTokenList.md)
- [Pagination](docs/Pagination.md)
- [Token](docs/Token.md)

## Usage

### Per-request configuration

All of the client methods accept an optional `RequestOptions` object.<br>This is
used if you want to set a [correlation ID](https://docs.basistheory.com/api-reference/?shell#request-correlation) or if you want to set a per-request [`X-API-KEY`](https://docs.basistheory.com/api-reference/?shell#authentication)

```python
import uuid
import basistheory
from basistheory.request_options import RequestOptions

request_options = RequestOptions(api_key="API KEY", correlation_id=uuid.uuid4())
```

### Client Configuration

Each Api client can be configured to use a custom API url and client-wide [`X-API-KEY`](https://docs.basistheory.com/api-reference/?shell#authentication).

```python
import basistheory
from basistheory.api import tokens_api

configuration = basistheory.Configuration(
    host = "https://token-proxy.somedomain.com",
    api_key = "API KEY"
)

with basistheory.ApiClient(configuration) as api_client:
    # Create a token client w/ global configuration for all requests
    token_client = tokens_api.TokensApi(api_client)
```