from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from examplecywebserviceapp.serviceappmodel.base_model import Model
from examplecywebserviceapp import util


class CyResultStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, status=None, message=None, progress=None, wall_time=None, start_time=None):  # noqa: E501
        """CyResultStatus - a model defined in OpenAPI

        :param id: The id of this CyResultStatus.  # noqa: E501
        :type id: str
        :param status: The status of this CyResultStatus.  # noqa: E501
        :type status: str
        :param message: The message of this CyResultStatus.  # noqa: E501
        :type message: str
        :param progress: The progress of this CyResultStatus.  # noqa: E501
        :type progress: int
        :param wall_time: The wall_time of this CyResultStatus.  # noqa: E501
        :type wall_time: int
        :param start_time: The start_time of this CyResultStatus.  # noqa: E501
        :type start_time: int
        """
        self.openapi_types = {
            'id': str,
            'status': str,
            'message': str,
            'progress': int,
            'wall_time': int,
            'start_time': int
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'message': 'message',
            'progress': 'progress',
            'wall_time': 'wallTime',
            'start_time': 'startTime'
        }

        self._id = id
        self._status = status
        self._message = message
        self._progress = progress
        self._wall_time = wall_time
        self._start_time = start_time

    @classmethod
    def from_dict(cls, dikt) -> 'CyResultStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CyResultStatus of this CyResultStatus.  # noqa: E501
        :rtype: CyResultStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CyResultStatus.

        Id of Cytoscape Service-App Request  # noqa: E501

        :return: The id of this CyResultStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CyResultStatus.

        Id of Cytoscape Service-App Request  # noqa: E501

        :param id: The id of this CyResultStatus.
        :type id: str
        """

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this CyResultStatus.

        Status of task can be (submitted,processing,complete,failed)  # noqa: E501

        :return: The status of this CyResultStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this CyResultStatus.

        Status of task can be (submitted,processing,complete,failed)  # noqa: E501

        :param status: The status of this CyResultStatus.
        :type status: str
        """
        allowed_values = ["submitted", "processing", "complete", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self) -> str:
        """Gets the message of this CyResultStatus.

        null or a message denoting a possible issue  # noqa: E501

        :return: The message of this CyResultStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this CyResultStatus.

        null or a message denoting a possible issue  # noqa: E501

        :param message: The message of this CyResultStatus.
        :type message: str
        """

        self._message = message

    @property
    def progress(self) -> int:
        """Gets the progress of this CyResultStatus.

        int between 0 and 100 denoting progress of task  # noqa: E501

        :return: The progress of this CyResultStatus.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress: int):
        """Sets the progress of this CyResultStatus.

        int between 0 and 100 denoting progress of task  # noqa: E501

        :param progress: The progress of this CyResultStatus.
        :type progress: int
        """

        self._progress = progress

    @property
    def wall_time(self) -> int:
        """Gets the wall_time of this CyResultStatus.

        Walltime in milliseconds task took to run  # noqa: E501

        :return: The wall_time of this CyResultStatus.
        :rtype: int
        """
        return self._wall_time

    @wall_time.setter
    def wall_time(self, wall_time: int):
        """Sets the wall_time of this CyResultStatus.

        Walltime in milliseconds task took to run  # noqa: E501

        :param wall_time: The wall_time of this CyResultStatus.
        :type wall_time: int
        """

        self._wall_time = wall_time

    @property
    def start_time(self) -> int:
        """Gets the start_time of this CyResultStatus.

        Time in milliseconds since 1969 epoch when task started  # noqa: E501

        :return: The start_time of this CyResultStatus.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: int):
        """Sets the start_time of this CyResultStatus.

        Time in milliseconds since 1969 epoch when task started  # noqa: E501

        :param start_time: The start_time of this CyResultStatus.
        :type start_time: int
        """

        self._start_time = start_time