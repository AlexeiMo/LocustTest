import os
from pathlib import Path
from helpers.assertion_helper import assert_status_code
from helpers.json_helper import read_json

filepath = os.path.abspath("target.json")
target = read_json(filepath)


def send_get_request(session, url, request_name, filename=None):
    if filename:
        source_file = Path("data") / filename
        params = read_json(source_file)
    else:
        params = None
    with session.get(url, name=request_name, params=params, verify=False,
                     catch_response=True) as response:
        assert_status_code(response)
        if response.content:
            return response.json()
