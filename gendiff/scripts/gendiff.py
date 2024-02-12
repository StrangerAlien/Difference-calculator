#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.argparser import parse_cli


# def main():
#     args = parse_cli()
#     diff = generate_diff(args.first_file, args.second_file, args.format)
#     print(diff)


def main():
    first, second, format_data = parse_cli()
    diff = generate_diff(first, second, format_data)
    print(diff)


if __name__ == '__main__':
    main()
