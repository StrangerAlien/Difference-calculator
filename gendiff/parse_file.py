import json
import yaml
import os.path as path


def get_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        extension = path.splitext(file_path)[1]
    return parse(data, extension)


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yml' or 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError('Unknown extension')
