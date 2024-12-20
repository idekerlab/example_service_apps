import unittest

from flask import json

from examplecywebserviceapp.serviceappmodel.cy_error_response import CyErrorResponse  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_meta_data import CyMetaData  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_request import CyRequest  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_request_id import CyRequestId  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_result import CyResult  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_result_status import CyResultStatus  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_server_status import CyServerStatus  # noqa: E501
from examplecywebserviceapp.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_delete_request(self):
        """Test case for delete_request

        Deletes task associated with {id} passed in
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_meta_data(self):
        """Test case for get_meta_data

        Gets meta data about this service/algorithm
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_request_status(self):
        """Test case for get_request_status

        Gets status of task
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/{id}/status'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_result(self):
        """Test case for get_result

        Gets result of task
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request(self):
        """Test case for request

        Submits task
        """
        cy_request = {"data":"{}","parameters":{"key":"parameters"},"algorithm":"updatetablesexample"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/',
            method='POST',
            headers=headers,
            data=json.dumps(cy_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status(self):
        """Test case for status

        Gets server status
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/status',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
