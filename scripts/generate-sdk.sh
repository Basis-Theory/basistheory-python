#!/bin/bash

docker pull openapitools/openapi-generator-cli:latest
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/swagger.json \
  -g python-prior \
  -o /local \
  -c /local/openapi-config.yml \
  --remove-operation-id-prefix

cd $(dirname $0)
cd ../