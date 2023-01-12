"""
    Basis Theory API

    ## Getting Started * Sign-in to [Basis Theory](https://basistheory.com) and go to [Applications](https://portal.basistheory.com/applications) * Create a Basis Theory Private Application * All permissions should be selected * Paste the API Key into the `BT-API-KEY` variable  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import basistheory
from basistheory.model.access_rule import AccessRule
globals()['AccessRule'] = AccessRule
from basistheory.model.authorize_session_request import AuthorizeSessionRequest


class TestAuthorizeSessionRequest(unittest.TestCase):
    """AuthorizeSessionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthorizeSessionRequest(self):
        """Test AuthorizeSessionRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthorizeSessionRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
