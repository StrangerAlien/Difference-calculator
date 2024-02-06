from gendiff.generate_diff import generate_diff

file1 = './tests/fixtures/file3.json'
file2 = './tests/fixtures/file4.json'


def test_plain_json():
    sample = './tests/fixtures/stylish.txt'

    with open(sample) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2) == sample_content
