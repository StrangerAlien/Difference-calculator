from gendiff.difference import get_diff
from gendiff.parse_file import get_data
from gendiff.formatting.stylish import stylish  # and all


def generate_diff(first_file_path, second_file_path, format_):
    diff = build_diff(first_file_path, second_file_path)
    return stylish(diff)


def build_diff(first_file_path, second_file_path):
    data1 = get_data(first_file_path)
    data2 = get_data(second_file_path)
    diff = get_diff(data1, data2)
    return diff
