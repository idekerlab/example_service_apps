from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from examplecywebserviceapp.serviceappmodel.base_model import Model
from examplecywebserviceapp import util


class CyWebMenuItemPath(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, gravity=None):  # noqa: E501
        """CyWebMenuItemPath - a model defined in OpenAPI

        :param name: The name of this CyWebMenuItemPath.  # noqa: E501
        :type name: str
        :param gravity: The gravity of this CyWebMenuItemPath.  # noqa: E501
        :type gravity: int
        """
        self.openapi_types = {
            'name': str,
            'gravity': int
        }

        self.attribute_map = {
            'name': 'name',
            'gravity': 'gravity'
        }

        self._name = name
        self._gravity = gravity

    @classmethod
    def from_dict(cls, dikt) -> 'CyWebMenuItemPath':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CyWebMenuItemPath of this CyWebMenuItemPath.  # noqa: E501
        :rtype: CyWebMenuItemPath
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CyWebMenuItemPath.

        Menu name  # noqa: E501

        :return: The name of this CyWebMenuItemPath.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CyWebMenuItemPath.

        Menu name  # noqa: E501

        :param name: The name of this CyWebMenuItemPath.
        :type name: str
        """

        self._name = name

    @property
    def gravity(self) -> int:
        """Gets the gravity of this CyWebMenuItemPath.

        Sets menu gravity, higher values mean lower on menu  # noqa: E501

        :return: The gravity of this CyWebMenuItemPath.
        :rtype: int
        """
        return self._gravity

    @gravity.setter
    def gravity(self, gravity: int):
        """Sets the gravity of this CyWebMenuItemPath.

        Sets menu gravity, higher values mean lower on menu  # noqa: E501

        :param gravity: The gravity of this CyWebMenuItemPath.
        :type gravity: int
        """

        self._gravity = gravity
