#!/usr/bin/env python3
from gendiff.difference import generate_diff
from gendiff.argparser import parse_cli


def main():
    args = parse_cli()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()

# poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
