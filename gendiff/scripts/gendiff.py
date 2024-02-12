#!/usr/bin/env python3
from gendiff.argparser import parse_cli
from gendiff import generate_diff


def main():
    args = parse_cli()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
