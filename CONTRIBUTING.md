# Contributing

## Prerequisites

First ensure you have python3 installed:

```shell
brew install python@3.10
```

Alternatively, you can use [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://github.com/asdf-vm/asdf) with the
[asdf-python plugin](https://github.com/asdf-community/asdf-python) to manage and switch between multiple versions 
of python locally. 

Next install dependencies using the command:

```shell
pip install .
```

## Updating the SDK

First download the latest API schema to `./swagger.json`, which can be done with the command:

```shell
make update-api-spec
```

Then regenerate the SDK using the open api generator with the command:

```shell
make generate-sdk
```

## Running tests

Copy the `./integration-tests/pytest.ini.example` file to `./integration-tests/pytest.ini` and enter a valid Basis Theory 
API url and API keys into this file.

To run tests using this configuration, run:

```shell
make verify
```

## Updating examples

The examples included under `/examples/resources` should be manually updated
with any new resources that are introduced.

After updating the examples, reformat and regenerate the markdown docs under 
`/docs/resources` by running the command:

```shell
go generate
```
