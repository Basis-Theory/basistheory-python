"""
    Basis Theory API

    ## Getting Started * Sign-in to [Basis Theory](https://basistheory.com) and go to [Applications](https://portal.basistheory.com/applications) * Create a Basis Theory Private Application * All permissions should be selected * Paste the API Key into the `BT-API-KEY` variable  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import basistheory
from basistheory.model.application import Application
globals()['Application'] = Application
from basistheory.model.patch_reactor_request import PatchReactorRequest


class TestPatchReactorRequest(unittest.TestCase):
    """PatchReactorRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchReactorRequest(self):
        """Test PatchReactorRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchReactorRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
