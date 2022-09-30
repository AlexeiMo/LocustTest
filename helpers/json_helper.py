import array
import json
from pathlib import Path


def read_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def write_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def update_json(filename, key, value):
    source_file = Path("data") / filename
    data = read_json(source_file)
    if type(key) == list:
        data[key[0]][key[1]] = value
    else:
        data[key] = value
    write_json(source_file, data)
