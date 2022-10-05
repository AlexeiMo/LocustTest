import os
from pathlib import Path
from helpers.assertion_helper import assert_status_code
from helpers.json_helper import read_json

filepath = os.path.abspath("target.json")
target = read_json(filepath)


def send_get_request(session, url, request_name, filename=None, user_id=None):
    if filename:
        source_file = Path("data") / filename
        params = read_json(source_file)
    else:
        params = None
    if user_id:
        params["userId"] = user_id
    with session.get(url, name=request_name, params=params, verify=False,
                     catch_response=True) as response:
        # print(response.content)
        assert_status_code(response)
        if response.content:
            return response.json()


def send_post_request(session, url, request_name, filename, status_code=200):
    source_file = Path("data") / filename
    with open(source_file, "rb") as data:
        with session.post(url, name=request_name, data=data, verify=False,
                          catch_response=True) as response:
            # print(response.content)
            assert_status_code(response, status_code)
            if response.content:
                return response.json()


def send_patch_request(session, url, request_name, filename, status_code=200):
    source_file = Path("data") / filename
    with open(source_file, "rb") as data:
        with session.patch(url, name=request_name, data=data, verify=False,
                           catch_response=True) as response:
            # print(response.content)
            assert_status_code(response, status_code)
            if response.content:
                return response.json()


def import_csv_file(session, url, request_name, filename):
    session.headers.update({"Content-Type": None})
    content_type = "text/csv"
    file_to_open = Path("data") / filename
    with open(file_to_open, "rb") as file:
        files = {"file": (filename, file, content_type)}
        with session.post(url, files=files, name=request_name,
                          verify=False, catch_response=True) as response:
            assert_status_code(response)
