from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from examplecywebserviceapp.serviceappmodel.base_model import Model
from examplecywebserviceapp import util


class CyInputNetwork(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, format=None, model=None):  # noqa: E501
        """CyInputNetwork - a model defined in OpenAPI

        :param format: The format of this CyInputNetwork.  # noqa: E501
        :type format: str
        :param model: The model of this CyInputNetwork.  # noqa: E501
        :type model: str
        """
        self.openapi_types = {
            'format': str,
            'model': str
        }

        self.attribute_map = {
            'format': 'format',
            'model': 'model'
        }

        self._format = format
        self._model = model

    @classmethod
    def from_dict(cls, dikt) -> 'CyInputNetwork':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CyInputNetwork of this CyInputNetwork.  # noqa: E501
        :rtype: CyInputNetwork
        """
        return util.deserialize_model(dikt, cls)

    @property
    def format(self) -> str:
        """Gets the format of this CyInputNetwork.

        Denotes format of returned data. 'cx2' returns CX2 format.  # noqa: E501

        :return: The format of this CyInputNetwork.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str):
        """Sets the format of this CyInputNetwork.

        Denotes format of returned data. 'cx2' returns CX2 format.  # noqa: E501

        :param format: The format of this CyInputNetwork.
        :type format: str
        """
        allowed_values = ["cx2", "edgelist"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def model(self) -> str:
        """Gets the model of this CyInputNetwork.

        Denotes network content returned. 'network' denotes full network data and 'graph' denotes bare network (ids only)  # noqa: E501

        :return: The model of this CyInputNetwork.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this CyInputNetwork.

        Denotes network content returned. 'network' denotes full network data and 'graph' denotes bare network (ids only)  # noqa: E501

        :param model: The model of this CyInputNetwork.
        :type model: str
        """
        allowed_values = ["network", "graph"]  # noqa: E501
        if model not in allowed_values:
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"
                .format(model, allowed_values)
            )

        self._model = model