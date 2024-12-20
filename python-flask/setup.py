import sys
from setuptools import setup, find_packages

NAME = "examplecywebserviceapp"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Cytoscape Service-App REST API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Cytoscape Service-App REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['examplecywebserviceapp=examplecywebserviceapp.__main__:main']},
    long_description="""\
    This [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) document defines the Cytoscape Service-App  REST Service API which is used by Cytoscape on the Web for Service-Apps.  This document and all references to the Cytoscape Service-App REST API, source code and ancillary documentation are copyrighted: *© 2013-2024,  The Regents of the University of California, The Cytoscape Consortium.  All rights reserved.*  Please abide with the  [Terms of Use, Licensing and Sources](https://home.ndexbio.org/disclaimer-license/). Likewise, the [Swagger-UI](https://github.com/swagger-api/swagger-ui)  document reader that displays this OpenAPI document is copyrighted by *Smartbear Software*. Its open-source software license is found  [here](https://github.com/swagger-api/swagger-ui/blob/master/LICENSE).  
    """
)

