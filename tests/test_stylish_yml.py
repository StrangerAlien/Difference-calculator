from gendiff.main import generate_diff

file1 = './tests/fixtures/file1.yml'
file2 = './tests/fixtures/file2.yml'


def test_stylish_json():
    sample = './tests/fixtures/stylish_1_2.txt'
    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2, 'stylish') == sample_content
