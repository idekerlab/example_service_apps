import uuid
import connexion
from time import time
from typing import Dict
from typing import Tuple
from typing import Union

from examplecywebserviceapp.serviceappmodel.cy_error_response import CyErrorResponse  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_meta_data import CyMetaData  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_request import CyRequest  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_request_id import CyRequestId  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_result import CyResult  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_result_status import CyResultStatus  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_server_status import CyServerStatus  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_web_menu_item import CyWebMenuItem  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_web_menu_item_path import CyWebMenuItemPath # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_service_input_definition import CyServiceInputDefinition  # noqa: E501
from examplecywebserviceapp.serviceappmodel.cy_input_network import CyInputNetwork  # noqa: E501
from examplecywebserviceapp import util

APP_VERSION='1.0'
CY_WEB_ACTION = 'updateTables'

TASK_DB = {}


def _current_time_millis():
    return int(time() * 1000)


def delete_request(id_=None):  # noqa: E501
    """Deletes task associated with {id} passed in

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if id_ in TASK_DB:
        del TASK_DB[id_]
        return None, 204

    return CyErrorResponse(message='Task not found'), 400


def get_meta_data():  # noqa: E501
    """Gets meta data about this service/algorithm

    Provides detailed information about algorithm offered by this Service-App # noqa: E501


    :rtype: Union[CyMetaData, Tuple[CyMetaData, int], Tuple[CyMetaData, int, Dict[str, str]]
    """
    params = None
    cywebmenuitem = CyWebMenuItem(root='Apps',
                                  path=[CyWebMenuItemPath(name='Example Service-Apps',
                                                          gravity=10),
                                        CyWebMenuItemPath(name='Python-Flask Add Column',
                                                          gravity=10)])
    inputnetwork = CyInputNetwork(model='network',
                                  format='cx2')
    serviceinputdefinition = CyServiceInputDefinition(type='network',
                                                      scope='dynamic',
                                                      input_network=inputnetwork)
    return CyMetaData(name='Example Python-Flask Service-App',
                      version=APP_VERSION,
                      description='Example Python-Flask Service-App that adds a new '
                                  'nodes column to current network',
                      author='Chris Churas',
                      email='NotSet',
                      citation='NA',
                      code_repository='https://github.com/idekerlab/example_service_apps',
                      tutorial='https://github.com/idekerlab/example_service_apps',
                      website='https://web-manual.cytoscape.org/',
                      parameters=params,
                      cy_web_actions=[CY_WEB_ACTION],
                      cy_web_menu_item=cywebmenuitem,
                      service_input_definition=serviceinputdefinition), 200


def get_request_status(id_=None):  # noqa: E501
    """Gets status of task

    This lets caller get status without getting the full result back # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[CyResultStatus, Tuple[CyResultStatus, int], Tuple[CyResultStatus, int, Dict[str, str]]
    """
    task = TASK_DB.get(id_)
    if task is None:
        return CyResultStatus(id=id_,
                              status='failed',
                              message='Task not found',
                              progress=100,
                              wall_time=0,
                              start_time=0), 400

    return CyResultStatus(id=id_,
                          status=task['status'],
                          message=task['message'],
                          progress=task['progress'],
                          wall_time=task['wall_time'],
                          start_time=task['start_time']), 200


def get_result(id_=None):  # noqa: E501
    """Gets result of task

    NOTE: For incomplete/failed jobs only Status, message, progress, and walltime will be returned in JSON # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[CyResult, Tuple[CyResult, int], Tuple[CyResult, int, Dict[str, str]]
    """
    task = TASK_DB.get(id_)
    if task is None:
        return CyResult(id=id_,
                        status='failed',
                        message='Task not found',
                        progress=100,
                        wall_time=0,
                        start_time=0,
                        result=None), 400

    return CyResult(id=id_,
                    status=task['status'],
                    message=task['message'],
                    progress=task['progress'],
                    wall_time=task['wall_time'],
                    start_time=task['start_time'],
                    result=task['result']), 200


def request(cy_request=None):  # noqa: E501
    """Submits task

    Payload in JSON format needs to have data along with name of algorithm to run and any algorithm specific parameters. Information about what algorithms are availableand what are the custom parameters can obtained by visiting the &#39;algorithms&#39;endpoint   The service should upon post return 202 and set location to resource to poll for result. Which will Match the URL of GET request below. # noqa: E501

    :param cy_request: Request as json
    :type cy_request: dict | bytes

    :rtype: Union[CyRequestId, Tuple[CyRequestId, int], Tuple[CyRequestId, int, Dict[str, str]]
    """
    if cy_request is None and connexion.request.is_json:
        cy_request = connexion.request.get_json()

    result_data = cy_request.get('data') if isinstance(cy_request, dict) else cy_request
    request_id = str(uuid.uuid4())
    start_time = _current_time_millis()
    TASK_DB[request_id] = {
        'status': 'complete',
        'message': None,
        'progress': 100,
        'wall_time': _current_time_millis() - start_time,
        'start_time': start_time,
        'result': [{'action': CY_WEB_ACTION, 'data': result_data}],
    }
    return CyRequestId(id=request_id), 202, {'Location': 'http://localhost:8080/example/' + request_id}


def status():  # noqa: E501
    """Gets server status

    Gets version, load, and diskusage of server # noqa: E501


    :rtype: Union[CyServerStatus, Tuple[CyServerStatus, int], Tuple[CyServerStatus, int, Dict[str, str]]
    """
    return CyServerStatus(status='ok', version=APP_VERSION)
