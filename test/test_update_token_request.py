"""
    Basis Theory API

    ## Getting Started * Sign-in to [Basis Theory](https://basistheory.com) and go to [Applications](https://portal.basistheory.com/applications) * Create a Basis Theory Server to Server Application * All permissions should be selected * Paste the API Key into the `BT-API-KEY` variable  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import basistheory
from basistheory.model.encryption_metadata import EncryptionMetadata
from basistheory.model.update_privacy import UpdatePrivacy
globals()['EncryptionMetadata'] = EncryptionMetadata
globals()['UpdatePrivacy'] = UpdatePrivacy
from basistheory.model.update_token_request import UpdateTokenRequest


class TestUpdateTokenRequest(unittest.TestCase):
    """UpdateTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateTokenRequest(self):
        """Test UpdateTokenRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateTokenRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()