import json
from typing import Union

import requests

from .logger import log_stdout
from logging import Logger

method_list = ['GET', 'PUT', 'POST', 'DELETE']


def redata_request(method: str, url: str, headers: dict, data: dict = None,
                   binary: bool = False, params: dict = None,
                   process: bool = True, log: Logger = log_stdout()) \
        -> Union[dict, requests.Response]:
    """
    Wrapper for common HTTP requests

    This code is based of a function in cognoma's figshare:
    https://github.com/cognoma/figshare

    :param method: HTTP method. One of GET, PUT, POST or DELETE
    :param url: URL for the request
    :param headers: HTTP header information
    :param data: HTTP data for PUT/POST
    :param binary: Whether data is binary or not
    :param params: Additional information for URL GET request
    :param process: Returns JSON content, otherwise the full request
                    is provided. Default: True
    :param log: Logger object for stdout and file logging. Default: stdout

    :return: JSON response for the request returned as python dict or
             the full request. See ``process`` option
    """

    if method not in method_list:
        log.warning("Incorrect method input provided!")
        log.warning(f"Must be one of these: {', '.join(method_list)}")
        raise ValueError

    if data is not None and not binary:
        data = json.dumps(data)

    response = requests.request(method, url, headers=headers,
                                data=data, params=params)

    if process:
        try:
            response.raise_for_status()
            try:
                response_data = json.loads(response.text)
            except ValueError:
                response_data = response.content
        except requests.exceptions.HTTPError as error:
            log.warning(f'Caught an HTTPError: {error}')
            log.warning('Body:\n', response.text)
            raise

        return response_data
    else:
        return response
