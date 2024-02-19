import pytest
import os
from gendiff import generate_diff


@pytest.fixture
def prepared_files(request):
    file1, file2, expected, format_name = request.param

    fixtures_path = os.path.join(os.path.dirname(__file__), "fixtures")

    with open(os.path.join(fixtures_path, expected)) as result_file:
        return (
            os.path.join(fixtures_path, file1),
            os.path.join(fixtures_path, file2),
            result_file.read(),
            format_name
        )


@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        ('file1.json', 'file2.json', 'result_stylish', 'stylish'),
        ('file1.yml', 'file2.yml', 'result_stylish', 'stylish'),
        ('file1.json', 'file2.json', 'result_plain', 'plain'),
        ('file1.yml', 'file2.yml', 'result_plain', 'plain'),
        ('file1.json', 'file2.json', 'result_json', 'json')
    ],
    indirect=True
)
def test_generate_diff(prepared_files):
    file1, file2, result_render, format_name = prepared_files

    assert result_render == generate_diff(file1, file2, format_name)
