#!/bin/bash
set -e

if [[ -z "${GIT_SHA}" ]]; then
    echo "GIT_SHA environment variable is not set"
    exit 1
fi

if [[ -z "${BT_API_KEY}" ]]; then
    echo "BT_API_KEY environment variable is not set"
    exit 1
fi

if [[ -z "${BT_MANAGEMENT_API_KEY}" ]]; then
    echo "BT_MANAGEMENT_API_KEY environment variable is not set"
    exit 1
fi

if [[ -z "${BT_BILLING_API_KEY}" ]]; then
    echo "BT_BILLING_API_KEY environment variable is not set"
    exit 1
fi

if [[ -z "${BT_CARD_REACTOR_ID}" ]]; then
    echo "BT_CARD_REACTOR_ID environment variable is not set"
    exit 1
fi

TEST_FILTER="BasisTheory.Vault.IntegrationTests"

if [[ -z "$IGNORE_AUTH0_TESTS" ]]; then
    if [[ -z "${CLIENT_ID}" ]]; then
        echo "CLIENT_ID environment variable is not set"
        exit 1
    fi
    
    if [[ -z "${AUTH0_SETTINGS}" ]]; then
        echo "AUTH0_SETTINGS environment variable is not set"
        exit 1
    fi
    
    AUTH0_CLIENT_ID=$(echo $AUTH0_SETTINGS | python3 -c "import sys, json; print(json.load(sys.stdin)['client_id'])")
    AUTH0_CLIENT_SECRET=$(echo $AUTH0_SETTINGS | python3 -c "import sys, json; print(json.load(sys.stdin)['client_secret'])")

    ACCESS_TOKEN_RESULT=$(curl --request POST --url https://basistheory-dev.us.auth0.com/oauth/token --header 'content-type: application/json' --data '{"client_id":"'$AUTH0_CLIENT_ID'","client_secret":"'$AUTH0_CLIENT_SECRET'","audience":"https://basistheory-dev.us.auth0.com/api/v2/","grant_type":"client_credentials"}')
    ACCESS_TOKEN=$(echo $ACCESS_TOKEN_RESULT | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")
    
    CLIENT_RESULT=$(curl -H "Authorization: Bearer $ACCESS_TOKEN" --url https://basistheory-dev.us.auth0.com/api/v2/clients/$CLIENT_ID?fields=client_secret&include_fields=true)
    export CLIENT_SECRET=$(echo $CLIENT_RESULT | python3 -c "import sys, json; print(json.load(sys.stdin)['client_secret'])")
    
    TEST_FILTER="BasisTheory.Vault.IntegrationTests"
else
    TEST_FILTER="DependsOn!=Auth0"
fi

current_directory="$PWD"

cd $(dirname $0)/..

echo "Running integration tests..."

dotnet restore -v=quiet
dotnet build BasisTheory.Vault.IntegrationTests/BasisTheory.Vault.IntegrationTests.csproj --no-restore -c Release -v=minimal
dotnet test BasisTheory.Vault.IntegrationTests/BasisTheory.Vault.IntegrationTests.csproj --no-build --no-restore -c Release -v=normal --logger "console;verbosity=detailed" --filter $TEST_FILTER

result=$?

cd "$current_directory"

exit $result
