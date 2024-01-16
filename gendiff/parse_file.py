import json
import yaml
import os.path as path


def get_data(file_paht):
    with open(file_paht, 'r') as file:
        data = file.read()
        extension = path.splitext(file_paht)[1]
    return parse(data, extension)


def parse(data, extension):
    if extension == 'json':
        return json.load(data)
    if extension == 'yml' or 'yaml':
        return yaml.safe_load(data)

# file1 = json.load(open('./tests/fixtures/file1.json'))
# file2 = json.load(open('./tests/fixtures/file2.json'))
