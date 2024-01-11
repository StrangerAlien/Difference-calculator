#!/usr/bin/env python3
from gendiff.difference import generate_diff
from gendiff.argparser import parse_cli
from gendiff.read_file import file1, file2


def main():
    parse_cli()
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
