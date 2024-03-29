"""
    Basis Theory API

    ## Getting Started * Sign-in to [Basis Theory](https://basistheory.com) and go to [Applications](https://portal.basistheory.com/applications) * Create a Basis Theory Private Application * All permissions should be selected * Paste the API Key into the `BT-API-KEY` variable  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import basistheory
from basistheory.model.three_ds_address import ThreeDSAddress
from basistheory.model.three_ds_cardholder_account_info import ThreeDSCardholderAccountInfo
from basistheory.model.three_ds_cardholder_authentication_info import ThreeDSCardholderAuthenticationInfo
from basistheory.model.three_ds_cardholder_phone_number import ThreeDSCardholderPhoneNumber
from basistheory.model.three_ds_prior_authentication_info import ThreeDSPriorAuthenticationInfo
globals()['ThreeDSAddress'] = ThreeDSAddress
globals()['ThreeDSCardholderAccountInfo'] = ThreeDSCardholderAccountInfo
globals()['ThreeDSCardholderAuthenticationInfo'] = ThreeDSCardholderAuthenticationInfo
globals()['ThreeDSCardholderPhoneNumber'] = ThreeDSCardholderPhoneNumber
globals()['ThreeDSPriorAuthenticationInfo'] = ThreeDSPriorAuthenticationInfo
from basistheory.model.three_ds_cardholder_info import ThreeDSCardholderInfo


class TestThreeDSCardholderInfo(unittest.TestCase):
    """ThreeDSCardholderInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testThreeDSCardholderInfo(self):
        """Test ThreeDSCardholderInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ThreeDSCardholderInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
