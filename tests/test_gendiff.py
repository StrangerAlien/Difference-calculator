# import pytest
from gendiff.difference import generate_diff
from gendiff.read_file import file1, file2


def test_plain():
    sample = './tests/fixtures/plain_result.txt'

    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2) == sample_content
