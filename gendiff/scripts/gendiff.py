#!/usr/bin/env python3
from gendiff import argparser
from gendiff.difference import generate_diff


def main():
    first, second, format_data = argparser.parse_cli()
    diff = generate_diff(first, second)
    print(diff)


if __name__ == '__main__':
    main()
