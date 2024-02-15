import pytest
from gendiff.generate_diff import generate_diff

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yml = 'tests/fixtures/file1.yml'
file2_yml = 'tests/fixtures/file2.yml'
result_plain = 'tests/fixtures/result_plain'
result_stylish = 'tests/fixtures/result_stylish'


@pytest.mark.parametrize(
    'file1, file2, format_, expected',
    [
        (file1_json, file2_json, "stylish", result_stylish),
        (file1_json, file2_json, "plain", result_plain),
        (file1_yml, file2_yml, "plain", result_plain),
        (file1_yml, file2_yml, "stylish", result_stylish)]
)
def test_generate_diff(file1, file2, format_, expected):
    assert generate_diff(file1, file2, format_) == open(expected).read()
