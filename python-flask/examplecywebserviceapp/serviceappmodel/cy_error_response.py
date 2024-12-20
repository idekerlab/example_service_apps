from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from examplecywebserviceapp.serviceappmodel.base_model import Model
from examplecywebserviceapp import util


class CyErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error_code=None, message=None, description=None, stack_trace=None, thread_id=None, time_stamp=None):  # noqa: E501
        """CyErrorResponse - a model defined in OpenAPI

        :param error_code: The error_code of this CyErrorResponse.  # noqa: E501
        :type error_code: str
        :param message: The message of this CyErrorResponse.  # noqa: E501
        :type message: str
        :param description: The description of this CyErrorResponse.  # noqa: E501
        :type description: str
        :param stack_trace: The stack_trace of this CyErrorResponse.  # noqa: E501
        :type stack_trace: str
        :param thread_id: The thread_id of this CyErrorResponse.  # noqa: E501
        :type thread_id: str
        :param time_stamp: The time_stamp of this CyErrorResponse.  # noqa: E501
        :type time_stamp: str
        """
        self.openapi_types = {
            'error_code': str,
            'message': str,
            'description': str,
            'stack_trace': str,
            'thread_id': str,
            'time_stamp': str
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'message': 'message',
            'description': 'description',
            'stack_trace': 'stackTrace',
            'thread_id': 'threadId',
            'time_stamp': 'timeStamp'
        }

        self._error_code = error_code
        self._message = message
        self._description = description
        self._stack_trace = stack_trace
        self._thread_id = thread_id
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'CyErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CyErrorResponse of this CyErrorResponse.  # noqa: E501
        :rtype: CyErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_code(self) -> str:
        """Gets the error_code of this CyErrorResponse.

        Error code to help identify issue  # noqa: E501

        :return: The error_code of this CyErrorResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str):
        """Sets the error_code of this CyErrorResponse.

        Error code to help identify issue  # noqa: E501

        :param error_code: The error_code of this CyErrorResponse.
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def message(self) -> str:
        """Gets the message of this CyErrorResponse.

        Human readable description of error  # noqa: E501

        :return: The message of this CyErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this CyErrorResponse.

        Human readable description of error  # noqa: E501

        :param message: The message of this CyErrorResponse.
        :type message: str
        """

        self._message = message

    @property
    def description(self) -> str:
        """Gets the description of this CyErrorResponse.

        More detailed description of error  # noqa: E501

        :return: The description of this CyErrorResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this CyErrorResponse.

        More detailed description of error  # noqa: E501

        :param description: The description of this CyErrorResponse.
        :type description: str
        """

        self._description = description

    @property
    def stack_trace(self) -> str:
        """Gets the stack_trace of this CyErrorResponse.

        Stack trace of error  # noqa: E501

        :return: The stack_trace of this CyErrorResponse.
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace: str):
        """Sets the stack_trace of this CyErrorResponse.

        Stack trace of error  # noqa: E501

        :param stack_trace: The stack_trace of this CyErrorResponse.
        :type stack_trace: str
        """

        self._stack_trace = stack_trace

    @property
    def thread_id(self) -> str:
        """Gets the thread_id of this CyErrorResponse.

        Id of thread running process  # noqa: E501

        :return: The thread_id of this CyErrorResponse.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id: str):
        """Sets the thread_id of this CyErrorResponse.

        Id of thread running process  # noqa: E501

        :param thread_id: The thread_id of this CyErrorResponse.
        :type thread_id: str
        """

        self._thread_id = thread_id

    @property
    def time_stamp(self) -> str:
        """Gets the time_stamp of this CyErrorResponse.

        UTC Time stamp in YYYY-MM-DD_HH:MM.S  # noqa: E501

        :return: The time_stamp of this CyErrorResponse.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: str):
        """Sets the time_stamp of this CyErrorResponse.

        UTC Time stamp in YYYY-MM-DD_HH:MM.S  # noqa: E501

        :param time_stamp: The time_stamp of this CyErrorResponse.
        :type time_stamp: str
        """

        self._time_stamp = time_stamp