import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format_, expected",
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", 'tests/fixtures/result_stylish'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "plain", 'tests/fixtures/result_plain'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "plain", 'tests/fixtures/result_plain'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/result_stylish')]
    )
def test_generate_diff(file1, file2, format_, expected):
    assert generate_diff(file1, file2, format_) == open(expected).read()
