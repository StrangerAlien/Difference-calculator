from gendiff.diff import generate_diff

file1 = './tests/fixtures/file1.yml'
file2 = './tests/fixtures/file2.yml'


def test_stylish_json():
    sample = './tests/fixtures/json_1_2.json'
    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2, 'json') == sample_content
