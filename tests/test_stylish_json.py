from gendiff.main import generate_diff


file1 = './tests/fixtures/file1.json'
file2 = './tests/fixtures/file2.json'
file3 = './tests/fixtures/file3.json'
file4 = './tests/fixtures/file4.json'


def test_stylish_json():
    sample_1_2 = './tests/fixtures/stylish_1_2.txt'
    with open(sample_1_2) as sample:
        sample_content = sample.read()
    assert generate_diff(file1, file2, 'stylish') == sample_content

    sample_3_4 = './tests/fixtures/stylish_3_4.txt'
    with open(sample_3_4) as sample:
        sample_content = sample.read()
    assert generate_diff(file3, file4, 'stylish') == sample_content
