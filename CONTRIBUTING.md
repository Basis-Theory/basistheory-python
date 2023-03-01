# Contributing

## Prerequisites

First ensure you have python3 installed:

```shell
brew install python@3.10
```

Alternatively, you can use [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf) with the
[asdf-python plugin](https://github.com/asdf-community/asdf-python) to manage and switch between multiple versions 
of python locally. 

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

### Install Dependencies

Next install dependencies using the command:

```shell
pip install .
```

## Updating the SDK

Download the latest API schema to `./swagger.json` from `https://api.basistheory.com/swagger/v1/swagger.json`, 
which can be done manually or with the command:

```shell
make update-api-spec
```

Once the latest api spec has been downloaded locally, you must regenerate the SDK using the open api generator,
which can be done with the command:

```shell
make generate-sdk
```

## Running tests

Copy the `./integration-tests/pytest.ini.example` file to `./integration-tests/pytest.ini` and enter configuration 
settings for a valid Basis Theory tenant.

- `BT_API_URL` is typically set to point to the dev environment: `https://api.flock-dev.com`
- `BT_API_KEY` should be set to an API key for a `private` application that can reveal data on read, search, and use and mask data on create, update, and delete.
- `BT_MANAGEMENT_API_KEY` should be set to an API key for a `management` application with all permissions.
- `BT_CARD_REACTOR_ID` should be set to the id of a Stripe card reactor, configured with a valid Stripe API key (either create your own Stripe account, or refer to 1pass for access to a shared account).


To run tests using this configuration, run:

```shell
make verify
```
