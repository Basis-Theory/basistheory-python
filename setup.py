"""
    BasisTheory Vault API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "basistheory"
VERSION = "0.14.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

# read contents from README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="BasisTheory Python SDK",
    author="Basis Theory",
    author_email="support@basistheory.com",
    url="https://basistheory.com",
    keywords=["BasisTheory", "Basis Theory", "SDK", "Python"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
      "Documentation": "https://docs.basistheory.com/",
      "Source Code": "https://github.com/Basis-Theory/basistheory-python",
    }
)
