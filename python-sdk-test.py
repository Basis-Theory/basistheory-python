import uuid
import basistheory
from pprint import pprint
from basistheory.api import tokens_api
from basistheory.model.token import Token
from basistheory.model.privacy import Privacy
from basistheory.request_options import RequestOptions

# Defining client wide api_key
configuration = basistheory.Configuration(
    api_key = "your_prod_key"
)

# Configuration for dev environment
configuration_dev = basistheory.Configuration(
  api_key= "key_dev_6x9AEckX5KPPrTS7Yf8tfj",
  host="https://api-dev.basistheory.com"
)

# Pass the configuration for prod/dev
with basistheory.ApiClient(configuration_dev) as api_client:
    # Create an instance of the tokens API client
    token_client = tokens_api.TokensApi(api_client)

    # Setting a correlation Id
    request_options = RequestOptions(correlation_id=uuid.uuid4().__str__())

    # Token request object
    privacy = Privacy(classification="general", impact_level="low", restriction_policy="redact")
    token = Token(type="token", data="My Secret Data", privacy=privacy)

    try:
        # Creating a token
        created_token = token_client.create(token=token, request_options=request_options)
        pprint(created_token)

        print("\n")

        # Retrieving it
        retrieved_token = token_client.get_by_id(id=created_token.id)
        pprint(retrieved_token)

        print("\n")

        # Listing my tokens
        tokens = token_client.list(page=1, size=1)
        pprint(tokens)

    except basistheory.ApiException as e:
        print("Exception when calling TokensApi: %s\n" % e)
