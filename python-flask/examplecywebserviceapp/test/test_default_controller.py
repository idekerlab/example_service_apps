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

    def _submit_request(self, data=None):
        cy_request = {
            "data": data if data is not None else {},
            "parameters": {"key": "parameters"},
            "algorithm": "updatetablesexample",
        }
        response = self.client.open(
            '/example',
            method='POST',
            data=json.dumps(cy_request),
            content_type='application/json')
        self.assertStatus(response, 202,
                          'Response body is : ' + response.data.decode('utf-8'))
        return json.loads(response.data.decode('utf-8'))['id']

    def test_delete_request(self):
        """Test case for delete_request

        Deletes task associated with {id} passed in
        """
        request_id = self._submit_request()
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example/{id}'.format(id=request_id),
            method='DELETE',
            headers=headers)
        self.assertStatus(response, 204,
                          'Response body is : ' + response.data.decode('utf-8'))

    def test_get_meta_data(self):
        """Test case for get_meta_data

        Gets meta data about this service/algorithm
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_request_status(self):
        """Test case for get_request_status

        Gets status of task
        """
        request_id = self._submit_request()
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example/{id}/status'.format(id=request_id),
            method='GET',
            headers=headers)
        self.assertStatus(response, 200,
                          'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(json.loads(response.data.decode('utf-8'))['status'], 'complete')

    def test_get_result(self):
        """Test case for get_result

        Gets result of task
        """
        request_id = self._submit_request()
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example/{id}'.format(id=request_id),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertEqual(json.loads(response.data.decode('utf-8'))['status'], 'complete')

    def test_get_result_returns_cx2_array_data(self):
        """Test case for getting result data as an action/data list"""
        cx2_data = [
            {"CXVersion": "2.0", "hasFragments": False},
            {"nodes": [{"id": 0, "v": {"name": "CAV1"}}]},
        ]
        request_id = self._submit_request(data=cx2_data)
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example/{id}'.format(id=request_id),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        result = json.loads(response.data.decode('utf-8'))['result']
        self.assertEqual(result[0]['action'], 'updateNetwork')
        self.assertIsInstance(result[0]['data'], list)
        node_aspects = [aspect['nodes'] for aspect in result[0]['data'] if 'nodes' in aspect]
        self.assertTrue(node_aspects)
        self.assertEqual(len(node_aspects[0]), 3)
        self.assertEqual(
            len([node for node in node_aspects[0]
                 if node['v']['name'].startswith('Random Node ')]),
            2)

    def test_request(self):
        """Test case for request

        Submits task
        """
        cy_request = {"data": {}, "parameters": {"key": "parameters"}, "algorithm": "updatetablesexample"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/example/',
            method='POST',
            headers=headers,
            data=json.dumps(cy_request),
            content_type='application/json')
        self.assertStatus(response, 202,
                          'Response body is : ' + response.data.decode('utf-8'))
        self.assertIn('/example/', response.headers.get('Location'))

    def test_request_accepts_serialized_json_data(self):
        """Test case for request with data passed as a serialized JSON object"""
        cy_request = {"data": "{}", "parameters": {"key": "parameters"}, "algorithm": "updatetablesexample"}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/example',
            method='POST',
            headers=headers,
            data=json.dumps(cy_request),
            content_type='application/json')
        self.assertStatus(response, 202,
                          'Response body is : ' + response.data.decode('utf-8'))
        self.assertIn('/example/', response.headers.get('Location'))

    def test_request_accepts_cx2_array_data(self):
        """Test case for request with data passed as a CX2 aspect array"""
        cy_request = {
            "algorithm": "updatetablesexample",
            "data": [
                {"CXVersion": "2.0", "hasFragments": False},
                {"nodes": [{"id": 0, "v": {"name": "CAV1"}}]},
            ],
            "parameters": {"key": "parameters"},
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/example',
            method='POST',
            headers=headers,
            data=json.dumps(cy_request),
            content_type='application/json')
        self.assertStatus(response, 202,
                          'Response body is : ' + response.data.decode('utf-8'))
        self.assertIn('/example/', response.headers.get('Location'))

    def test_status(self):
        """Test case for status

        Gets server status
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/example/status',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
